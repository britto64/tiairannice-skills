---
name: criativos-com-ia
description: >-
  Produz criativos de marketing de ponta a ponta com o Claude e seus conectores: pega o roteiro pronto, gera a
  locução com a voz da marca (ElevenLabs), junta os vídeos da marca ou gera imagens e vídeos (Higgsfield), monta o
  vídeo por código (Remotion), e sobe os anúncios na Meta ou entrega o vídeo pronto para o TikTok. Também gera lotes
  de anúncios estáticos a partir de referências (Black Friday e outras datas), edita vídeo com IA e orienta quais
  conectores ligar. Use sempre que o usuário quiser transformar um roteiro em vídeo ou anúncio, produzir imagem,
  vídeo, narração ou arte com IA, subir criativos na Meta, ganhar tempo de produção ou montar seu estúdio criativo,
  mesmo sem citar nenhuma ferramenta.
---

# Criativos com IA

O Claude conduz a produção do roteiro até o anúncio no ar, usando os conectores ligados à conversa: voz, geração de
imagem e vídeo, montagem de vídeo e publicação. A ideia central: **o resultado vem do briefing e da conferência de
qualidade**; as ferramentas executam. Quem decide permissões, créditos e publicação são o app e os conectores, e a
skill cuida de fazer bem o trabalho.

Os arquivos em `references/` guardam o método de cada etapa. Leia o certo antes de responder, em vez de resumir de
memória.

## Primeiro: veja o que está conectado

Liste as ferramentas disponíveis na conversa (voz, geração de imagem e vídeo, Meta, publicação, ambiente de código)
e monte o fluxo com elas. Se faltar algo, produza o que for possível (roteiro, prompts, textos, pacote de entrega) e
diga em uma linha qual conector ligar para automatizar o resto. Veja `references/conectores-e-ferramentas.md`.

## O fluxo: do roteiro ao ar

1. **Roteiro de produção.** Quebre o roteiro (da skill `roteiros-de-video`) em cenas, com fala, imagem e texto na
   tela. Se houver briefing da marca (skill `gestor-de-marketing`), use-o; peça só o que faltar.
2. **Locução.** Gere a fala com a voz da marca no conector de voz, direto no chat, em trechos curtos.
3. **Material visual.** Use os vídeos da marca que o usuário enviar e gere o que faltar (b-roll, produto em cena,
   imagens de anúncio) com o conector de geração.
4. **Montagem.** Junte locução, vídeos, legendas e elementos da marca por código (Remotion ou semelhante),
   exportando os formatos necessários e assistindo ao resultado inteiro.
5. **Pacote de entrega.** Arquivos por formato, textos (anúncio ou legenda), chamada para ação e variações de gancho.
6. **Publicação.** Anúncios: suba na Meta pelo conector, seguindo o plano da skill `meta-ads`. Orgânico: publique
   no TikTok pelo conector, se houver, ou entregue o arquivo e a legenda prontos.
7. **Medir e repetir.** O criativo vencedor vira variações; o perdedor sai.

O fluxo completo, com as tabelas e os modelos de cada etapa, está em `references/fluxo-do-roteiro-ao-ar.md`.

## Qual arquivo ler

| Situação do usuário | Arquivo |
|---|---|
| Tem um roteiro e quer vídeo ou anúncio pronto e publicado; vídeos da marca para montar | `references/fluxo-do-roteiro-ao-ar.md` |
| Gerar vários anúncios de imagem; anúncios de Black Friday; subir criativos na Meta | `references/anuncios-estaticos-com-ia.md` |
| Cortar, legendar e montar vídeo; reduzir o tempo de edição | `references/edicao-de-video-com-ia.md` |
| Locução da marca; clonar voz; documento em áudio; dublagem | `references/voz-e-audio.md` |
| Quais conectores e ferramentas existem e o que cada um faz | `references/conectores-e-ferramentas.md` |

## Princípios

- **Briefing antes de ferramenta.** O mesmo pedido detalhado serve em qualquer ferramenta; a ferramenta muda, o
  briefing não.
- **Referências boas valem mais que prompts longos.** Mostre exemplos do que gosta e peça inspiração de layout.
- **A duração do áudio comanda a montagem.** Gere a locução primeiro e corte as cenas para caber nela.
- **Confira a qualidade do que sai:** produto fiel, texto sem erro em português, preço e prazo corretos, legendas
  na posição certa. Corrija pontos específicos em vez de refazer tudo.
- **Uma peça primeiro, depois o lote.** Um anúncio, um vídeo de 30 segundos, uma locução; ao acertar o padrão,
  escale.
- **Variações são a regra.** Cada peça boa vira 3 versões de gancho para testar (ver a skill `meta-ads`).

## Notas

- Resultados citados nas referências (faturamento com anúncios de IA, tempo de edição, custo por imagem) são relatos
  de criadores, que em geral também divulgam as ferramentas. Use como ordem de grandeza.
- Nomes, planos e funções das ferramentas mudam rápido. Esta skill foi montada de vídeos de out/2026.
