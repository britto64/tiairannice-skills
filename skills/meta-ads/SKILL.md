---
name: meta-ads
description: >-
  Planeja, revisa e diagnostica anúncios no Meta Ads (Facebook e Instagram) para negócios: estrutura de campanha,
  criativos que performam (avatar específico, três níveis de dor, ganchos), volume e variações de anúncios,
  públicos e remarketing, funil e oferta para quem não conhece a marca, orçamento e escala, métricas (ROAS de
  equilíbrio, CAC, LTV) e plano de verba para Black Friday e outras datas fortes. Use sempre que o usuário falar
  de tráfego pago, anúncio, campanha, verba, orçamento, público, lookalike, remarketing, ROAS, CPM, criativo de
  anúncio, impulsionar, Black Friday ou "meu anúncio não vende", mesmo sem citar Meta.
---

# Meta Ads

Ajuda a planejar e melhorar anúncios no Facebook e no Instagram. A ideia central, segundo os gestores estudados:
hoje o que mais pesa é o **criativo** (quem ele descreve e que problema resolve), seguido de **volume e variedade**
de anúncios, de uma **oferta e página que convencem quem não conhece a marca** e de **regras claras de verba**. O
que está em `references/` detalha cada ponto; leia o arquivo certo antes de responder, em vez de resumir de
memória.

## Como trabalhar

1. **Levante os dados antes de recomendar.** Se houver um briefing da marca (a skill `gestor-de-marketing` o
   salva), use-o. Se houver acesso à conta de anúncios (conector), consulte os números reais. Caso contrário,
   peça de uma vez só: objetivo (venda, lead, mensagem), preço e margem do produto, verba mensal disponível,
   histórico de anúncios (o que já rodou e deu certo ou errado), onde a pessoa converte (site, WhatsApp, loja),
   estoque e capacidade de atender, e data limite se for campanha sazonal.
2. **Calcule o ponto de equilíbrio** (ROAS de equilíbrio e CAC máximo), pois sem isso não há meta de verdade. O
   método está em `references/metricas-e-escala.md`.
3. **Escolha a lente** na tabela abaixo. Um pedido costuma precisar de duas ou três.
4. **Entregue um plano** (formato abaixo) com valores em reais, datas reais e a ordem do que fazer.
5. **Encaminhe** o que sai do escopo: roteiros e ganchos de vídeo para `roteiros-de-video`, produção de criativos
   com IA para `criativos-com-ia`, oferta, marca e conteúdo para `marca-e-posicionamento`, plano completo de mês
   ou campanha para `gestor-de-marketing`.

## Qual arquivo ler

| Situação do usuário | Arquivo |
|---|---|
| Criar ou revisar anúncios; "meu anúncio não converte"; ganchos e ângulos | `references/criativos-que-performam.md` |
| Quantos anúncios; cansaço de criativo; ideias; copiar o que funciona dos concorrentes | `references/volume-e-variacoes.md` |
| Para quem anunciar; remarketing; públicos semelhantes; segmentação ampla | `references/publicos-e-segmentacao.md` |
| Clica e não compra; trabalhar com quem nunca ouviu falar da marca; garantia; WhatsApp | `references/funil-e-oferta-para-trafego-frio.md` |
| Black Friday, Natal, Dia das Mães, qualquer data forte | `references/black-friday-e-datas-fortes.md` |
| Quanto gastar; quando aumentar a verba; ROAS, CAC, LTV; diagnóstico da conta | `references/metricas-e-escala.md` |

## Formato do plano de Meta Ads

```
Objetivo e meta (em reais): 
Ponto de equilíbrio (ROAS e CAC máximo):
Estrutura de campanhas (contínua / promoção / remarketing), com a verba de cada uma:
Públicos (novos, remarketing, semelhantes) e o que testar primeiro:
Criativos: lista de personas × ângulos × ganchos, formatos e quantos por semana:
Funil e conversão (página ou WhatsApp, prova, garantia, tempo de resposta):
Regras de escala (quando aumentar, quando pausar, janela de avaliação):
Calendário com datas reais e responsáveis:
Métricas de acompanhamento e frequência de revisão:
Riscos e premissas (o que foi suposto por falta de dados):
```

## Princípios que valem sempre

- **O criativo é o alvo.** Fale com uma pessoa específica sobre uma situação específica; evite anúncio que serve
  "para todo mundo".
- **Uma dor na altura certa.** Anuncie a situação que o problema impede de viver, não só o nome do problema.
- **Volume com variedade.** Muitos formatos, ganchos e personas; quando achar um vencedor, multiplique-o.
- **Confiança antes da venda para quem é novo.** Prova, garantia e resposta rápida substituem a indicação.
- **Meta de verdade tem conta.** Defina o ROAS de equilíbrio e só aumente a verba quando a meta for atingida.
- **Datas fortes pedem investimento antes**: não corte a verba do mês anterior à promoção.

## Cuidados

- Os números das referências (volumes de anúncios, percentuais de aumento de verba, LTV:CAC) são relatos de
  gestores de fora do Brasil, em geral de e-commerce ou serviços de ticket alto. Use como ordem de grandeza e
  adapte à verba e ao porte do negócio; não os prometa ao usuário.
- Nunca prometa ROAS, CAC ou resultado. Depende de nicho, preço, margem, execução e concorrência.
- Aumentos agressivos de verba só fazem sentido com histórico e retorno comprovado. Em conta pequena ou nova, vá
  devagar.
- As políticas e as opções da Meta mudam. Confirme as regras atuais (atributos pessoais, saúde, antes e depois,
  promoções) e as opções de público que existem hoje na conta.
- Em saúde, nutrição e estética, não prometa resultado nem sugira que sabe a condição da pessoa.
- Esta skill foi montada a partir de vídeos de out/2026; recomendações específicas de plataforma envelhecem rápido.
