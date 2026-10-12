# Instalar as skills (instruções para o Claude)

Se o usuário enviou o link deste repositório e pediu para instalar as skills, siga estes passos.

## Endereços diretos dos pacotes

Repositório: https://github.com/britto64/tiairannice-skills

- https://raw.githubusercontent.com/britto64/tiairannice-skills/main/dist/gestor-de-marketing.skill
- https://raw.githubusercontent.com/britto64/tiairannice-skills/main/dist/marca-e-posicionamento.skill
- https://raw.githubusercontent.com/britto64/tiairannice-skills/main/dist/meta-ads.skill
- https://raw.githubusercontent.com/britto64/tiairannice-skills/main/dist/roteiros-de-video.skill
- https://raw.githubusercontent.com/britto64/tiairannice-skills/main/dist/criativos-com-ia.skill

## 1. Pegue os pacotes

Cada skill pronta tem um pacote `dist/<nome>.skill` (um zip). Baixe todos os `.skill` da pasta `dist/` deste
repositório, usando os endereços diretos acima (ou, se o link recebido for de outro repositório, o mesmo caminho nele).

- Se `dist/` estiver vazio, as skills ainda estão em construção: avise o usuário e não instale nada.
- Se não conseguir baixar pelo ambiente (sem acesso à internet), peça ao usuário para baixar os `.skill` pela
  página do repositório e enviá-los na conversa.
- Se tiver o repositório inteiro (clone ou zip), rode `python3 scripts/empacotar.py` para gerar os pacotes.

## 2. Instale todos juntos

Instale todos os pacotes que estiverem em `dist/`. A `gestor-de-marketing` consulta as outras skills, então
instalar só uma delas deixa o fluxo incompleto.

Para cada pacote:

- Se você tem uma ferramenta para entregar arquivos ao usuário, apresente o `.skill`. O usuário clica em
  salvar e a skill entra na conta dele.
- Se não tem, diga ao usuário para abrir a área de Skills nas configurações do app, enviar cada `.skill` e
  ativá-las.

## 3. Confirme que funcionou

Peça ao usuário para testar com: "preciso planejar o mês de Black Friday". A `gestor-de-marketing` deve começar
fazendo perguntas sobre a marca (site, objetivo, oferta, público, formatos de filmagem, verba). Se ela não
disparar, confira se o usuário ativou as skills e se a opção de skills está habilitada na conta dele.
