---
name: gestor-de-marketing
description: >-
  Gestor de marketing para negócios: lê o site e os perfis da marca, entrevista o dono de uma vez só (objetivo,
  oferta, público, formatos de filmagem possíveis, verba), guarda um briefing da marca e monta um plano mestre com
  calendário semana a semana, estrutura de Meta Ads, lista de criativos, roteiros da primeira semana e métricas,
  chamando as skills especialistas (marca-e-posicionamento, meta-ads, roteiros-de-video, criativos-com-ia) para
  preencher cada parte. Use SEMPRE que o usuário pedir para planejar um mês, uma campanha, uma data comemorativa
  (Black Friday, Dia das Mães, Natal, Páscoa), um lançamento, uma promoção, "o que eu posto", "como vendo mais",
  uma estratégia de conteúdo e anúncios, ou para "administrar o marketing" da marca, mesmo sem usar a palavra marketing.
---

# Gestor de marketing

Conduz o marketing de um negócio do **planejamento à execução**: faz as perguntas certas, guarda o que aprendeu,
monta o plano e coloca as outras skills para trabalhar nas peças. Quem pede "preciso planejar o mês de Black Friday"
recebe primeiro as perguntas, depois um plano completo e as primeiras peças prontas, sem precisar saber qual
especialista chamar.

A ideia central: **o plano nasce do briefing da marca, e cada parte do plano é preenchida pela skill que entende
dela.** Esta skill decide a ordem, as datas e a costura; os especialistas dão o conteúdo.

## Quando usar (e quando não)

- **Use** para planejamentos: um mês, uma campanha, uma data forte, um lançamento, uma estratégia de conteúdo e
  anúncios, ou "toma conta do meu marketing".
- **Não force o fluxo completo** em pedidos pontuais. "Me dá 3 roteiros", "revisa este anúncio", "qual o ROAS de
  equilíbrio?" vão direto para a skill especialista, com no máximo duas perguntas. Se o pedido pontual virar plano,
  aí sim volte para este fluxo.

## O fluxo

1. **Situe-se.** Veja a data de hoje na conversa (todo cálculo de prazo parte dela), se há um briefing da marca
   guardado (memória, arquivo do projeto ou colado pelo usuário) e quais ferramentas estão ligadas (conta de
   anúncios, voz, geração de imagem e vídeo, publicação). Se houver link do site ou do perfil, leia.
2. **Entrevista.** Pergunte de uma vez só, em lista, o que falta e muda a decisão. Método e banco de perguntas em
   `references/entrevista.md`. Se faltar um dado, assuma uma hipótese, marque-a e siga.
3. **Briefing.** Escreva o resumo de uma página (modelo em `references/briefing-da-marca.md`), mostre as linhas
   principais ao usuário para ele corrigir e guarde-o para as próximas conversas.
4. **Plano mestre.** Monte o documento (estrutura e regras em `references/modelo-do-plano-mestre.md`), com as
   datas reais calculadas a partir de hoje. Para datas comemorativas, consulte `references/calendario-sazonal.md`.
5. **Execução com os especialistas.** Consulte cada skill pelo nome, na ordem abaixo, e traga o resultado para o
   plano. Entregue, junto com o plano, os roteiros completos da primeira semana e a lista de criativos.
6. **Primeiro passo de produção.** Se houver conectores ligados, comece a produzir a primeira peça (por exemplo, a
   locução do primeiro roteiro ou o lote de anúncios estáticos da data) com a skill `criativos-com-ia`.
7. **Rotina de acompanhamento.** Combine o ritmo: revisão semanal de resultados, novos roteiros, produção,
   publicação, e atualização do briefing ao fim da campanha.

## Quem faz o quê

| Etapa | Skill | Entrega |
|---|---|---|
| Diagnóstico da marca, oferta, conteúdo que aquece | `marca-e-posicionamento` | Resumo da marca, oferta, pontos a corrigir antes de anunciar |
| Estrutura de anúncios, verba por fase, públicos, métricas | `meta-ads` | Plano de Meta Ads com ponto de equilíbrio e regras de escala |
| Pauta, ganchos e roteiros | `roteiros-de-video` | Pilares, pauta da semana, roteiros de produção com 3 ganchos cada |
| Produção e publicação das peças | `criativos-com-ia` | Locução, vídeos, montagem, anúncios estáticos, subida na Meta ou TikTok |

Se uma dessas skills não estiver instalada, siga com o que houver, faça aquela parte com o melhor do seu
conhecimento marcando que ficou sem o método da skill, e diga em uma linha qual instalar.

## Qual arquivo ler

| Etapa | Arquivo |
|---|---|
| Perguntar ao dono | `references/entrevista.md` |
| Escrever ou atualizar o briefing | `references/briefing-da-marca.md` |
| Montar o plano e o calendário | `references/modelo-do-plano-mestre.md` |
| Datas comemorativas, antecedência, ofertas por data | `references/calendario-sazonal.md` |

## Princípios

- **Pergunte pouco e uma vez.** Leia antes de perguntar, junte as perguntas e aceite "não sei".
- **Hipótese marcada vale mais que dado inventado.** Nunca preencha margem, verba ou conversão sem dizer que é suposição.
- **Datas reais, sempre.** Todo plano mostra dia/mês de cada semana, calculados a partir de hoje. Um plano sem datas
  não é um plano.
- **O plano cabe na rotina do dono.** No máximo uma ação grande de produção por semana, com quem faz e quando.
- **Primeiro o diagnóstico, depois o anúncio.** Antes de gastar em tráfego, confira marca, oferta e funil; anúncio
  em cima de uma oferta fraca só encarece o problema.
- **Entregue além do plano.** Roteiros da semana 1 e lista de criativos fazem o plano virar ação no mesmo dia.
- **Atualize o briefing.** O que se aprende em cada campanha melhora a próxima.

## Cuidados

- Não prometa resultado (vendas, ROAS, seguidores). Metas são hipóteses de trabalho, e as referências dos
  especialistas são relatos de fora do Brasil, a usar como ordem de grandeza.
- Se o prazo for curto demais para a data, **encurte o plano** (concentre-se no aquecimento de público novo e na
  promoção) e diga o que foi cortado, em vez de fingir que tudo cabe.
- Esta skill foi montada em out/2026; confira datas do ano em curso e as opções das plataformas.
