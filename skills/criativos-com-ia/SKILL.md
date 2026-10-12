---
name: criativos-com-ia
description: >-
  Produção de criativos e conteúdo com IA para negócios: gerar anúncios estáticos em lote a partir de referências
  (inclusive Black Friday), editar vídeo com ajuda da IA (cortes, legendas, animação), clonar a própria voz para
  locuções, transformar documentos em áudio, e montar um estúdio criativo com o Claude usando skills e conectores
  (pesquisa de concorrentes, escrita na sua voz, geração de imagem e vídeo). Use sempre que o usuário quiser
  produzir anúncio, imagem, vídeo, narração ou arte com IA, ganhar tempo de produção, decidir quais ferramentas
  ligar ao Claude ou subir criativos na conta de anúncios, mesmo sem citar nenhuma ferramenta.
---

# Criativos com IA

Ajuda a produzir anúncios, vídeos e áudios com o Claude e ferramentas ligadas a ele, mais rápido e sem perder a
identidade da marca. A ideia central: **a IA executa; o resultado depende do briefing e da revisão humana.** Quem
briefa bem (marca, oferta exata, referências, formato) e revisa com cuidado ganha horas. Quem aceita o primeiro
resultado publica erro.

Os arquivos em `references/` guardam o método de cada tipo de produção. Leia o certo antes de responder, em vez de
resumir de memória.

## Como trabalhar

1. **Entenda o que será produzido e para quê.** Anúncio estático, vídeo, locução ou montagem de estúdio? Qual
   objetivo e onde será publicado? Se houver briefing da marca (a skill `gestor-de-marketing` o salva), use-o.
2. **Garanta que há o que gerar.** Antes de produzir, confirme: a oferta exata (preço, prazo, condições), a
   persona e a dor que o criativo toca (ver as skills `meta-ads` e `marca-e-posicionamento`), as referências
   visuais, as cores, o logo e as fotos reais do produto. Sem isso, a IA inventa.
3. **Leia o arquivo do tipo de produção** (tabela abaixo) e monte o pedido com o modelo dele.
4. **Gere em pequeno lote, revise com a lista de conferência e só então escale.** Corrija pontos específicos em
   vez de refazer tudo.
5. **Encaminhe**: teste e verba na skill `meta-ads`; roteiros e ganchos na skill `roteiros-de-video`; plano geral na
   skill `gestor-de-marketing`.

## Qual arquivo ler

| Situação do usuário | Arquivo |
|---|---|
| Gerar vários anúncios de imagem; anúncios de Black Friday; subir criativos na conta; referências de concorrentes | `references/anuncios-estaticos-com-ia.md` |
| Cortar, legendar e montar vídeo; reduzir o tempo de edição | `references/edicao-de-video-com-ia.md` |
| Locução sem regravar; clonar a própria voz; documento em áudio | `references/voz-clonada-e-audio.md` |
| Quais ferramentas, skills e conectores ligar; escolher e instalar com segurança | `references/ferramentas-e-skills-para-claude.md` |

## Princípios que valem sempre

- **Briefing antes de ferramenta.** O mesmo pedido detalhado serve em qualquer ferramenta; a ferramenta muda, o
  briefing não.
- **Referências boas valem mais que prompts longos.** Mostre exemplos do que gosta; peça inspiração de layout, nunca
  cópia.
- **Revise tudo o que vai ao público**: produto fiel, texto sem erro em português, preço e prazo corretos,
  promessas dentro das regras.
- **Dê ao agente a menor autoridade necessária.** Crie em pausa, com limite de gasto, e ative você mesmo.
- **Comece com uma peça, depois escale.** Um anúncio, um vídeo de 30 segundos, uma locução.

## Cuidados

- **Skills e conectores de terceiros são código de terceiros.** Leia antes de instalar, dê acesso mínimo e nunca
  cole chaves de acesso em conversas ou repositórios. Detalhes em `references/ferramentas-e-skills-para-claude.md`.
- **Acesso de escrita à conta de anúncios** pode gastar dinheiro. Exija pausa, revisão humana e teto de gasto.
- **Voz e imagem de pessoas**: só use com autorização por escrito; não simule falas nem depoimentos falsos.
- **Direitos**: música, fontes, imagens e referências com licença adequada; inspiração não é cópia.
- **Resultados citados** (faturamento com anúncios de IA, tempo de edição, custo por imagem) são relatos de
  criadores, em geral de quem também vende as ferramentas. Não os prometa ao usuário.
- **Preços, planos e nomes de ferramentas mudam rápido.** Esta skill foi montada de vídeos de out/2026; confirme
  o que existe hoje na conta do usuário.
