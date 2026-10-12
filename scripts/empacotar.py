#!/usr/bin/env python3
"""Empacota cada pasta de skills/ em dist/<nome>.skill (zip que o app do Claude aceita).

Uso:
  python3 scripts/empacotar.py              gera/atualiza os pacotes em dist/
  python3 scripts/empacotar.py --verificar  só confere se dist/ está em dia (sai com erro se não estiver)

Regras que o app impõe e que este script confere antes de empacotar:
  - exatamente um SKILL.md por skill, na raiz da pasta dela
  - frontmatter só com name, description, license, allowed-tools, metadata, compatibility
  - name em kebab-case (até 64 caracteres) e igual ao nome da pasta
  - description preenchida, até 1024 caracteres, sem os sinais de menor e maior

Skill que ainda contém o marcador EM CONSTRUÇÃO é pulada de propósito: o repositório é público
e dist/ é o que o Claude instala, então rascunho não pode entrar nele.

Os zips são determinísticos (mesma ordem, mesma data): se nada mudou, os bytes são idênticos
e o Git não mostra diferença.
"""
import argparse
import re
import sys
import zipfile
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Falta o PyYAML: pip install pyyaml")

RAIZ = Path(__file__).resolve().parent.parent
MARCADOR_RASCUNHO = "EM CONSTRUÇÃO"
PERMITIDOS = {"name", "description", "license", "allowed-tools", "metadata", "compatibility"}
EXCLUIR_EM_QUALQUER_NIVEL = {"__pycache__", "node_modules"}
EXCLUIR_NA_RAIZ = {"evals"}
EXCLUIR_ARQUIVOS = {".DS_Store", "Thumbs.db"}
DATA_FIXA = (2026, 1, 1, 0, 0, 0)


def arquivos_da_skill(pasta: Path):
    for p in sorted(pasta.rglob("*")):
        if not p.is_file() or p.name in EXCLUIR_ARQUIVOS or p.suffix == ".pyc":
            continue
        rel = p.relative_to(pasta)
        if any(parte in EXCLUIR_EM_QUALQUER_NIVEL for parte in rel.parts):
            continue
        if len(rel.parts) > 1 and rel.parts[0] in EXCLUIR_NA_RAIZ:
            continue
        yield p, rel


def validar(pasta: Path):
    """Devolve (situacao, mensagem). situacao: 'ok', 'rascunho' ou 'erro'."""
    skill_md = pasta / "SKILL.md"
    if not skill_md.exists():
        return "erro", "falta o SKILL.md"
    extras = [rel for p, rel in arquivos_da_skill(pasta) if rel.name == "SKILL.md" and len(rel.parts) > 1]
    if extras:
        return "erro", f"SKILL.md extra em {', '.join(map(str, extras))} (o app aceita só um por skill)"
    texto = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", texto, re.DOTALL)
    if not m:
        return "erro", "frontmatter ausente ou mal formado"
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        return "erro", f"YAML inválido no frontmatter: {e}"
    if not isinstance(fm, dict):
        return "erro", "o frontmatter precisa ser um dicionário YAML"
    sobra = set(fm) - PERMITIDOS
    if sobra:
        return "erro", f"chave(s) não permitida(s) no frontmatter: {', '.join(sorted(sobra))}"
    nome, desc = fm.get("name"), fm.get("description")
    if not isinstance(nome, str) or not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", nome) or len(nome) > 64:
        return "erro", f"name inválido: {nome!r} (kebab-case, até 64 caracteres)"
    if nome != pasta.name:
        return "erro", f"name '{nome}' difere do nome da pasta '{pasta.name}'"
    if not isinstance(desc, str) or not desc.strip():
        return "erro", "description vazia"
    if len(desc.strip()) > 1024:
        return "erro", f"description com {len(desc.strip())} caracteres (máximo 1024)"
    if "<" in desc or ">" in desc:
        return "erro", "description não pode ter os sinais de menor ou maior"
    for p, rel in arquivos_da_skill(pasta):
        if rel.suffix == ".md" and MARCADOR_RASCUNHO in p.read_text(encoding="utf-8"):
            return "rascunho", f"marcador '{MARCADOR_RASCUNHO}' em {rel}"
    return "ok", "ok"


def gerar_zip(pasta: Path, destino: Path):
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        for p, rel in arquivos_da_skill(pasta):
            info = zipfile.ZipInfo(f"{pasta.name}/{rel.as_posix()}", DATA_FIXA)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, p.read_bytes())


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--verificar", action="store_true", help="não escreve nada; confere se dist/ está em dia")
    ap.add_argument("--skills", default=str(RAIZ / "skills"), help="pasta com as skills (padrão: skills/)")
    ap.add_argument("--saida", default=str(RAIZ / "dist"), help="pasta dos pacotes (padrão: dist/)")
    args = ap.parse_args()

    skills_dir, saida = Path(args.skills), Path(args.saida)
    pastas = sorted(p for p in skills_dir.iterdir() if p.is_dir() and not p.name.startswith("."))
    if not pastas:
        sys.exit(f"nenhuma skill em {skills_dir}")

    problemas, esperados = [], set()
    for pasta in pastas:
        situacao, msg = validar(pasta)
        if situacao == "erro":
            problemas.append(f"{pasta.name}: {msg}")
            print(f"  ERRO      {pasta.name}: {msg}")
            continue
        if situacao == "rascunho":
            print(f"  rascunho  {pasta.name}: pulada ({msg})")
            continue
        esperados.add(f"{pasta.name}.skill")
        alvo = saida / f"{pasta.name}.skill"
        if args.verificar:
            tmp = saida / f".{pasta.name}.tmp"
            saida.mkdir(parents=True, exist_ok=True)
            gerar_zip(pasta, tmp)
            em_dia = alvo.exists() and alvo.read_bytes() == tmp.read_bytes()
            tmp.unlink()
            print(f"  {'em dia   ' if em_dia else 'DESATUALIZADO'} {alvo.name}")
            if not em_dia:
                problemas.append(f"{alvo.name} desatualizado ou ausente")
        else:
            saida.mkdir(parents=True, exist_ok=True)
            antes = alvo.read_bytes() if alvo.exists() else None
            gerar_zip(pasta, alvo)
            print(f"  {'igual    ' if antes == alvo.read_bytes() else 'gerado   '} {alvo.name}")

    # pacote em dist/ sem skill correspondente pronta (removida ou voltou a rascunho)
    sobras = sorted(p.name for p in saida.glob("*.skill") if p.name not in esperados) if saida.exists() else []
    for nome in sobras:
        if args.verificar:
            problemas.append(f"{nome} está em dist/ mas a skill não está pronta")
        else:
            (saida / nome).unlink()
            print(f"  removido  {nome} (skill não está pronta)")

    if problemas:
        print("\nProblemas:\n  " + "\n  ".join(problemas))
        sys.exit(1)
    print(f"\n{len(esperados)} pacote(s) pronto(s) em {saida}" if esperados else "\nNenhuma skill pronta ainda (todas em rascunho).")


if __name__ == "__main__":
    main()
