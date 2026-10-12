# Conectores e ferramentas do estúdio

Estudado em out/2026. Use para saber o que cada conector faz e qual usar em cada etapa. Nomes, planos e funções
mudam rápido: **antes de planejar, veja quais ferramentas estão disponíveis na conversa** e monte o fluxo com o que
existe. Para o que não estiver ligado, produza o material pronto (roteiro, prompts, textos) e diga ao usuário o que
conectar para automatizar o resto.

## O estúdio por etapa

| Etapa | O que resolve | Conectores e ferramentas citados nos vídeos |
|---|---|---|
| Pesquisa de concorrentes | Ver mensagens, ganchos e chamadas que estão rodando agora | Skill que extrai anúncios de concorrentes; biblioteca de anúncios da Meta |
| Pesquisa de mercado | Análise em várias etapas, em segundo plano | Skills de pesquisa profunda (esboço aprovado, depois investigação) |
| Escrita na voz da marca | Texto novo que soa como a marca | Skill que extrai o ritmo das frases e o vocabulário de textos existentes |
| Pesquisa e redação com fontes | Texto com citações e checagem de fatos | Skills de redação com pesquisa |
| Imagem e vídeo gerados | Criativos, b-roll, produto em cena | Conector Higgsfield (ver abaixo) |
| Voz | Locução, narração, documento em áudio | Conector ElevenLabs |
| Montagem de vídeo | Cortes, legendas, animação, explicativos | Remotion, Hyperframes; ffmpeg; transcrição local |
| Limpeza de gravação | Tirar vícios, pausas e tentativas repetidas | Descript |
| Música e efeitos | Trilha e sons | Conectores de músicas e efeitos (como o Artlist) |
| Anúncios | Subir e gerenciar campanhas | Conector da Meta para anúncios |
| Orgânico | Publicar no TikTok | Conector de publicação (no Higgsfield) ou entrega do arquivo |
| Relações públicas | Pauta, pitch e lista de jornalistas | Skills de PR digital (ver a skill `marca-e-posicionamento`) |

## O que o conector de imagem e vídeo costuma oferecer

Exemplo do Higgsfield, conforme as ferramentas que ele expõe (confira o que sua conta mostra):

- **Gerar imagens e vídeos** com vários modelos; escolhe-se o modelo pelo uso (anúncios de produto, vídeo geral,
  cenas com vários planos, retratos).
- **Estúdio de anúncios**: com o kit da marca (logo, paleta, tom), produtos e objetivo, gera lotes de conceitos
  prontos nos formatos 1:1, 9:16, 16:9 e 3:4.
- **Estúdio de shorts**: reestiliza um vídeo enviado em vários clipes curtos verticais.
- **Reenquadrar** um vídeo para outro formato; **ampliar** resolução; **remover fundo**.
- **Dublagem e troca de voz**; **análise de potencial de viralização** de um vídeo pronto (gancho, atenção, retenção).
- **Publicação no TikTok**, com formulário de revisão antes de postar.
- Para quem produz bastante, existe também acesso por API com cobrança por uso, uma alternativa à assinatura fixa;
  compare com os seus volumes.

Itens de compatibilidade úteis: o gerador de anúncios não faz 4:5 (oferece 3:4); imagens geradas saem em PNG e o
TikTok só aceita foto em JPEG ou WebP, então converta antes de publicar.

## O que o conector da Meta faz

Permite ao Claude ler o desempenho de campanhas e criar ou alterar campanhas, conjuntos e anúncios na conta, e
subir criativos. O caminho que os criadores usam: indicar um anúncio modelo da conta, deixar o Claude copiar as
configurações e trocar só o criativo e os textos. A estratégia (estrutura, verba, públicos, testes) está na skill
`meta-ads`.

## Como escolher o que ligar primeiro

1. **Comece pelo gargalo.** Onde o tempo ou a qualidade pesa mais: referências, texto, imagem, vídeo ou voz?
2. **Uma etapa de cada vez.** Um estúdio com dez ferramentas pela metade rende menos que três bem usadas.
3. **Comece pelo trio que fecha o ciclo:** voz (locução), geração de imagem e vídeo, e o conector da Meta (ou o de
   publicação). Com ele, do roteiro ao anúncio no ar cabe em uma conversa. A montagem por código entra quando
   houver vídeos gravados para juntar.
4. **Compare custo fixo e por uso** de acordo com o seu volume de produção.
5. **Teste com uma peça** (um anúncio, um vídeo de 30 segundos, uma locução) antes de montar a rotina.

## Quando falta uma ferramenta

- Sem conector de voz: entregue o roteiro falado, com pontuação para narração, e os trechos numerados.
- Sem conector de geração: entregue prompts prontos, no modelo de `anuncios-estaticos-com-ia.md`.
- Sem conector da Meta: entregue o pacote de entrega (arquivos, textos, variações) e a estrutura de campanha para
  o usuário subir.
- Sem ambiente de código: entregue o roteiro de produção e o briefing de edição, que servem para qualquer editor.
