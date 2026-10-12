# Edição e montagem de vídeo com IA

Estudado em out/2026. Use quando o usuário quer cortar, legendar, animar ou montar vídeos com ajuda da IA, ou
reduzir o tempo de edição. As ferramentas mudam rápido; o que permanece é a ordem das etapas. Para o fluxo
completo (roteiro, voz, material, publicação), veja `fluxo-do-roteiro-ao-ar.md`.

## A ideia: é uma cadeia de etapas, não um botão

A edição por IA funciona quando é feita em sequência: limpar a gravação → definir estilo → sincronizar som e imagens
→ complementar → conferir. Pular o briefing e esperar o resultado final pronto costuma frustrar.

## Caminho A: tudo por código, no próprio computador

Um criador relata ter editado um vídeo inteiro em cerca de 30 minutos assim, pedindo a um agente de código:

1. **Transcrever** a gravação com um modelo de transcrição aberto, que roda no computador e é gratuito.
2. **Cortar e converter** com ffmpeg: remover pausas, juntar trechos, ajustar formato e imagem.
3. **Montar com código** (Remotion, Hyperframes ou semelhantes): legendas, textos animados, gráficos, cartão final.
4. **Conferir** o vídeo inteiro: no caso relatado, as legendas saíram um pouco mal posicionadas e foi preciso pedir
   ajuste.

## Caminho B: com conectores

Roteiro de 7 passos comum entre criadores:

| Passo | O que fazer |
|---|---|
| 1. Modelo | Usar o modelo mais capaz que a conta oferece (montar por código exige raciocínio) |
| 2. Ferramenta de montagem por código | Adicionar uma skill para montar vídeo por código (Remotion ou semelhante) |
| 3. Limpar a gravação | Se há vícios de fala, silêncios e várias tentativas, usar uma ferramenta de edição por transcrição (como o Descript) para limpar antes |
| 4. Fontes | Dar imagens das fontes que quer e pedir que o agente as instale |
| 5. Moodboard e briefing | Reunir referências visuais e de movimento e escrever um briefing curto |
| 6. Som e voz | Conectores de música e efeitos, de locução e de imagens de apoio geradas por IA para cenas que não foram gravadas |
| 7. Falar o que imagina | Ligar o ditado e descrever em voz a edição que quer |

Com o conector de geração de vídeo, também dá para **reestilizar** um vídeo enviado (por exemplo, virar vários clipes
curtos em um estilo escolhido) e **reenquadrar** um vídeo para outro formato.

## Montagem por código: estrutura que funciona

- **Uma composição por formato** (9:16, 4:5, 1:1), com as cenas do roteiro de produção em ordem.
- **A duração de cada cena sai da locução.** Gere o áudio primeiro, meça cada trecho e corte os clipes para caber.
- **Legendas por palavra**, com os tempos vindos da transcrição do áudio final. Estilo da marca, 1 a 3 linhas,
  em área segura, com contraste.
- **Tipografia e cores da marca** em todos os textos; logo discreto; cartão final com oferta e chamada.
- **Transições simples.** Corte seco costuma funcionar melhor do que efeitos em vídeo curto.
- **Música** baixa sob a voz.
- **Exportar** em cada formato, com nome claro (`nome-9x16.mp4`).

## Briefing de edição (modelo)

```
Objetivo do vídeo (vender, ensinar, divulgar, bastidor):
Onde vai ser publicado e formato (Reels/TikTok/Shorts, 9:16, duração máxima):
Quem fala e o tom (direto, brincalhão, calmo):
Ritmo: cortes rápidos ou mais respiro? Quantos segundos por cena?
Legenda: estilo, cor e posição (fora das áreas cobertas pela interface da plataforma):
Fontes e cores da marca:
Referências visuais (3 a 5) e o que gostei em cada uma:
Música e efeitos:
Locução: voz e roteiro:
O que NÃO fazer:
```

## Boas práticas

- **Limpe antes de estilizar.** Cortar vícios e erros no início economiza retrabalho.
- **Deixe referências falarem.** "Quero no clima disto" funciona melhor que adjetivos soltos.
- **Peça uma versão rápida primeiro** (rascunho de 30 segundos), depois refine o vídeo todo.
- **Assista ao vídeo inteiro** depois de cada versão: ortografia das legendas, posição, sincronia, volume da música
  sobre a voz, áreas seguras da tela e fidelidade ao roteiro.
- **Guarde o briefing** e reaproveite: um mesmo estilo em vários vídeos constrói identidade (ver a skill
  `marca-e-posicionamento`).
- Tempos prometidos ("30 minutos", "1 minuto") são os dos criadores, com bom briefing e material. Planeje com folga.
