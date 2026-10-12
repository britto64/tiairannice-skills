# Do roteiro ao ar

Estudado em out/2026. Use quando o usuário já tem (ou acabou de montar) um roteiro e quer transformá-lo em vídeo ou
anúncio publicado, usando os conectores que estiverem ligados ao Claude. Este é o fluxo principal da skill: os
outros arquivos detalham cada etapa.

```
roteiro → locução → material visual → montagem → pacote de entrega → publicação → medir e repetir
```

## Entradas que o fluxo precisa

Reúna estas informações antes de começar. O que já estiver no briefing da marca (skill `gestor-de-marketing`) ou no
roteiro, não pergunte de novo; peça o resto de uma vez só.

- **Roteiro** (ou peça à skill `roteiros-de-video` para escrever).
- **Destino**: anúncio na Meta, orgânico no TikTok ou Reels, ou os dois.
- **Formato e duração**: vertical 9:16, feed 4:5 ou quadrado 1:1; duração alvo.
- **Voz**: qual voz usar na locução (a voz da marca, se já existir no conector de voz).
- **Material da marca**: vídeos gravados, fotos do produto, logo, cores e fontes.
- **Oferta e chamada para ação** exatas (preço, prazo, para onde a pessoa vai: WhatsApp, site, loja).

## Etapa 1: transformar o roteiro em roteiro de produção

Quebre o roteiro em cenas, uma por frase ou ideia, em uma tabela. Essa tabela guia todo o resto.

| Cena | Tempo | Fala (locução) | Imagem | Texto na tela |
|---|---|---|---|---|
| 1 | 0 a 3 s | Gancho | Plano de impacto (rosto, produto, resultado) | Frase curta do gancho |
| 2 | 3 a 10 s | Problema | Clipe da marca ou imagem gerada | Palavra-chave |
| 3 | ... | ... | ... | ... |
| Final | últimos 3 a 5 s | Chamada para ação | Produto e contato | Oferta e botão/endereço |

Regra prática: uma imagem nova ou um corte a cada 2 a 4 segundos mantém o ritmo em vídeo curto. As estruturas de
roteiro e os ganchos estão na skill `roteiros-de-video`.

## Etapa 2: locução

Gere a locução com o conector de voz, direto no chat, usando a voz da marca. Gere por cena ou em trechos curtos,
ouça e fixe a versão. A **duração do áudio define a duração de cada cena** na montagem. Veja `voz-e-audio.md`.

## Etapa 3: material visual

**A) Vídeos da marca enviados pelo usuário.** Catalogue os clipes: nome, duração, o que mostram, qualidade. Se não
conseguir ver o vídeo, extraia quadros e a transcrição (ffmpeg e um modelo de transcrição) ou pergunte ao usuário.
Case cada clipe com a cena do roteiro de produção; os melhores ficam no gancho e no fecho.

**B) Complementos gerados.** Para o que não foi gravado (cenas de apoio, produto em ambiente, fundos, animações),
gere imagens e vídeos curtos com o conector de geração. Use sempre fotos reais do produto como referência e peça no
formato final. Veja `anuncios-estaticos-com-ia.md` para o modelo de pedido.

**C) Ajuste de formato.** Se um vídeo precisa virar outro formato (de horizontal para vertical, por exemplo), use a
ferramenta de reenquadramento do conector ou refaça o corte na montagem.

## Etapa 4: montagem

Monte tudo em código com uma ferramenta de vídeo por código (Remotion ou semelhante). Estrutura que funciona:

1. **Uma composição por formato**, com as cenas na ordem do roteiro de produção.
2. **A duração de cada cena vem do áudio** da locução; os clipes são cortados para caber.
3. **Legendas sincronizadas** a partir da transcrição do áudio gerado (com os tempos de cada palavra), em fonte e
   cor da marca, dentro da área segura da tela (longe das bordas e dos botões da plataforma).
4. **Elementos de marca**: logo discreto, cores e fontes; cartão final com a oferta e a chamada para ação.
5. **Música** em volume baixo sob a voz, quando houver.
6. **Exportar** em cada formato necessário e **assistir ao resultado inteiro** antes de entregar.

Detalhes de técnica em `edicao-de-video-com-ia.md`.

Antes de publicar, se houver no conector uma ferramenta de análise de vídeo (por exemplo, para estimar força do
gancho e retenção), use-a no vídeo pronto e ajuste o gancho se preciso.

## Etapa 5: pacote de entrega

O que o usuário (ou o conector de publicação) precisa receber:

- Os arquivos finais, nomeados por formato (`nome-9x16.mp4`, `nome-4x5.mp4`).
- **Texto principal, título e chamada para ação** (para anúncio) ou **legenda e hashtags** (para orgânico).
- **2 ou 3 variações de gancho** (os primeiros 3 segundos) para testar, com a cena 1 trocada.
- Um resumo de uma linha: objetivo, público, oferta, formato.

## Etapa 6: publicação

**Anúncio na Meta.** Use o conector da Meta para subir os criativos conforme a estrutura do plano de anúncios
(skill `meta-ads`: campanha, conjuntos e públicos). O caminho que os criadores descrevem: indicar um anúncio que o
usuário já montou na conta, para o Claude copiar as configurações e trocar só o criativo e os textos.

**Orgânico no TikTok.** Se o conector de publicação estiver ligado, use-o com legenda e formato certos. Caso
contrário, entregue o arquivo e a legenda prontos para o usuário postar. Formatos que o TikTok costuma aceitar:
vídeo MP4, MOV ou WebM, de 3 segundos a 10 minutos, com pelo menos 360 px de largura e de altura e de 23 a 60
quadros por segundo; fotos em JPEG ou WebP (PNG precisa ser convertido).

**Reels e outras redes.** Entregue o arquivo vertical e a legenda.

## Etapa 7: medir e repetir

Acompanhe os resultados e volte ao topo: o criativo vencedor vira variações (outro gancho, outro cenário, outra
locução) e o perdedor sai. A rotina semanal e as regras de teste estão na skill `meta-ads`; os ganchos novos, na
skill `roteiros-de-video`.

## Receitas rápidas

| Quero... | Caminho |
|---|---|
| Anúncio de vídeo com locução e os vídeos da marca | Roteiro de produção → locução → clipes da marca → montagem → pacote → subir na Meta |
| Vídeo explicativo sem material gravado | Roteiro → locução → imagens e vídeos gerados + animações em código → montagem |
| Lote de anúncios de imagem para uma data | Direto em `anuncios-estaticos-com-ia.md` |
| Reaproveitar um vídeo vencedor | Reenquadrar para outros formatos, trocar gancho e locução, publicar como variação |
| Orgânico para TikTok | Roteiro → locução → vídeos da marca → montagem 9:16 → legenda → publicar |

## Formatos de referência

| Uso | Proporção | Medida usual |
|---|---|---|
| Reels, Stories, TikTok, Shorts | 9:16 | 1080 × 1920 |
| Feed da Meta (retrato) | 4:5 | 1080 × 1350 |
| Quadrado | 1:1 | 1080 × 1080 |

Confirme as medidas atuais de cada plataforma e as proporções que o conector de geração aceita (algumas ferramentas
não geram 4:5 e oferecem 3:4 ou 1:1; nesse caso, recorte na montagem).
