# Edição de vídeo com IA

Estudado em out/2026. Use quando o usuário quer cortar, legendar, animar ou montar vídeos com ajuda da IA, ou
reduzir o tempo de edição. As ferramentas mudam rápido; o que permanece é a ordem das etapas.

## A ideia: é uma cadeia de etapas, não um botão

A edição por IA funciona quando é feita em sequência: limpar a gravação → definir estilo → sincronizar som e
imagens → complementar → revisar. Pular o briefing e esperar o resultado final pronto costuma frustrar.

## Caminho A: tudo local e sem assinatura

Um criador relata ter editado um vídeo inteiro em cerca de 30 minutos assim, pedindo a um agente de código:

1. **Transcrever** a gravação com um modelo de transcrição aberto, que roda no próprio computador e é gratuito.
2. **Cortar e converter** com ffmpeg: remover pausas, juntar trechos, ajustar formato e imagem.
3. **Montar com código** (por exemplo Remotion): legendas, textos animados, gráficos.
4. **Revisar**: o resultado teve legendas um pouco mal posicionadas, então olhar o vídeo inteiro e pedir ajuste.

Vantagens: sem custo de assinatura e o vídeo bruto não sai do seu computador (bom para material de cliente).

## Caminho B: com conectores e ferramentas externas

Um roteiro de 7 passos, comum entre criadores:

| Passo | O que fazer |
|---|---|
| 1. Modelo | Usar o modelo mais capaz que sua conta oferece (editar com código exige raciocínio) |
| 2. Ferramenta de edição por código | Adicionar uma skill para montar vídeo por código (Remotion ou semelhante) |
| 3. Limpar a gravação | Se há vícios de fala, silêncios e várias tentativas, usar uma ferramenta de edição por transcrição (como Descript) para limpar antes |
| 4. Fontes | Dar imagens das fontes que quer e pedir que o agente as instale |
| 5. Moodboard e briefing | Reunir referências visuais (e de motion) e escrever um briefing curto |
| 6. Som e voz | Conectores de música e efeitos, de locução (voz sintética) e de imagens de apoio geradas por IA para cenas que você não gravou |
| 7. Falar o que imagina | Ligar o ditado e descrever em voz a edição que quer |

## Briefing de edição (modelo)

```
Objetivo do vídeo (vender, ensinar, divulgar, bastidor):
Onde vai ser publicado e formato (Reels/TikTok/Shorts, 9:16, duração máxima):
Quem fala e o tom (direto, brincalhão, calmo):
Ritmo: cortes rápidos ou mais respiro? Quantos segundos por cena?
Legenda: estilo, cor e posição (fora das áreas cobertas pela interface da plataforma):
Fontes e cores da marca:
Referências visuais (3 a 5) e o que gostei em cada uma:
Música e efeitos: com direito de uso comercial. Voz: a minha / sintética com autorização:
O que NÃO fazer:
```

## Boas práticas

- **Limpe antes de estilizar.** Cortar vícios e erros no início economiza retrabalho.
- **Deixe referências falarem.** "Quero no clima disto" funciona melhor que adjetivos soltos.
- **Peça uma versão rápida primeiro** (rascunho de 30 segundos) antes de refinar o vídeo todo.
- **Revise sempre**: legendas e textos (ortografia, posição), sincronia, volume da música sobre a voz, áreas
  seguras da tela e fidelidade ao que foi dito.
- **Guarde o briefing** e reaproveite: um mesmo estilo em vários vídeos constrói identidade (ver
  `marca-e-posicionamento`).

## Cuidados

- **Privacidade**: não envie material de clientes, de menores ou de terceiros para serviços externos sem
  autorização; prefira o caminho local.
- **Direitos**: use música, fontes e imagens com licença comercial. Conteúdo gerado por IA pode ter regras
  próprias de uso em anúncios.
- **Voz sintética**: ver `voz-clonada-e-audio.md`.
- **Conectores variam** por conta e por plano, e alguns exigem um ambiente de código; confirme o que está disponível.
- **Tempo prometido** ("30 minutos", "1 minuto") é o do criador, com bom briefing e material. Planeje com folga.
