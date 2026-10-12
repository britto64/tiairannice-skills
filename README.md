# Skills de marketing para o Claude

Um conjunto de skills em português para o Claude administrar o marketing de um negócio: você diz
"preciso planejar o mês de Black Friday" e ele faz perguntas sobre a marca, monta um plano completo e
chama os especialistas para detalhar anúncios, públicos, criativos e roteiros de vídeo.

> **Status:** as 5 skills estão prontas e os pacotes estão em `dist/`. O conteúdo foi montado em out/2026; datas e
> opções das plataformas mudam, então confirme o que vale hoje.

## As skills

| Skill | Para quê |
|---|---|
| `gestor-de-marketing` | A maestra. Entrevista o dono (site, objetivo, oferta, público, formatos de filmagem, verba), monta o plano mestre e aciona as demais. |
| `marca-e-posicionamento` | Quem é a marca, para quem fala, qual transformação entrega, tom de voz, psicologia do cliente. |
| `meta-ads` | Estrutura de campanha, orçamento (incluindo datas fortes), públicos, criativos e métricas no Meta Ads. |
| `roteiros-de-video` | Ganchos, estruturas de storytelling, formatos de vídeo, retenção e pauta semanal de conteúdo. |
| `criativos-com-ia` | Voz clonada, edição e geração de criativos com IA, passo a passo. |

Instale as cinco juntas: a `gestor-de-marketing` conta com as outras quatro para detalhar cada parte do plano.

## Como instalar

Envie o link deste repositório para o Claude e peça para instalar. Ele segue o [INSTALAR.md](INSTALAR.md).

Se preferir fazer à mão: baixe os arquivos `.skill` da pasta [`dist/`](dist/) e envie cada um na área de
Skills das configurações do app do Claude.

## Como usar

Depois de instaladas, basta pedir o que precisa:

- "Preciso planejar o mês de Black Friday"
- "Me dá os roteiros de vídeo da semana"
- "Monta a estrutura de campanha no Meta Ads para o lançamento"

## O que há aqui (e o que não há)

O conteúdo das skills é conhecimento reescrito e organizado em instruções, estruturas, exemplos e modos de
aplicar. Não há transcrições nem cópias de vídeos de terceiros. Os números e resultados citados pelos
criadores de conteúdo são tratados como referência, nunca como promessa.

## Para quem mantém o repositório

```
skills/<nome>/SKILL.md      cada skill (um SKILL.md por skill; detalhes em references/)
dist/<nome>.skill           pacotes prontos, gerados pelo script
scripts/empacotar.py        valida e gera os pacotes
```

Depois de editar qualquer skill, rode `python3 scripts/empacotar.py` e inclua `dist/` no commit.
`python3 scripts/empacotar.py --verificar` confere se `dist/` está em dia. Skills que ainda contêm o marcador
`EM CONSTRUÇÃO` são puladas de propósito e nunca entram em `dist/`.
