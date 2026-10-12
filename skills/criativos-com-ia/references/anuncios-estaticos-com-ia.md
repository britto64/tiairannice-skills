# Anúncios estáticos com IA

Estudado em out/2026. Use quando o usuário quer gerar vários anúncios de imagem de uma vez (produto, promoção,
Black Friday) a partir de referências, e depois subi-los na Meta. As ferramentas e os preços mudam rápido; o método
abaixo é o que permanece. Resultados citados pelos criadores (como "mais de 30 mil dólares com imagens geradas por
IA") são relatos sem verificação.

## A receita em uma frase

Um pedido bem montado, com **marca, oferta exata, referências de layout, persona e formato**, devolve de 5 a 10
anúncios sólidos em poucos minutos, usando o Claude com um conector de geração de imagem. O trabalho passa a ser
**briefar bem e conferir a qualidade**, não desenhar.

## Dois caminhos

1. **Estúdio de anúncios do conector** (quando existir, como o do Higgsfield): você informa a marca (logo, paleta e
   tom ficam no kit da marca), os produtos, o objetivo (vendas, leads, tráfego, reconhecimento) e o formato; ele
   escreve os conceitos e gera as imagens. Bom para volume e para manter a identidade da marca.
2. **Geração de imagem com referências**: um pedido detalhado ao conector de imagem, com as referências anexadas.
   Dá mais controle sobre layout e texto. É o caminho do modelo abaixo.

## Modelo de pedido (adapte e cole no Claude)

```
Crie [N] anúncios para [marca / promoção], usando [conector de imagem].

Marca: site [endereço]. Use as cores e o logo da marca e a foto EXATA do produto que está no site.
Oferta: [texto exato, ex.: "30% de desconto em todo o site até 30/11"]. Não invente preços nem condições.
Pessoa e situação: [persona e a dor ou situação que o produto resolve].
Ângulos: proponha ângulos e escolha os com maior chance de converter, dizendo por quê.
Referências: anexei [3 a 4] anúncios de marcas do mesmo ramo, como inspiração de layout e de estilo.
Mistura: metade com a oferta no título e o botão de chamada na parte de baixo, perto do produto;
  metade com um título criativo sobre o produto e a oferta em segundo plano.
Formato: [4:5 para feed / 9:16 para stories e reels]. Idioma: português do Brasil, com acentos corretos.
Pode gerar tudo. Antes, faça no máximo 5 perguntas se faltar algo essencial. Ao final, devolva uma tabela com
persona, ângulo e título de cada anúncio.
```

Por que cada parte importa:

| Parte | Motivo |
|---|---|
| Foto exata do produto | A IA não inventa um produto parecido; mantém a fidelidade |
| Oferta em texto exato | Evita preço, prazo ou condição inventados |
| Referências de layout | Dão um ponto de partida de design que já funciona no ramo |
| Persona e ângulo | Sem isso o anúncio fica genérico (ver a skill `meta-ads`, criativos que performam) |
| Dois tipos de anúncio | Permite testar oferta pura contra título criativo |
| Perguntas antes de gerar | O agente se alinha em vez de adivinhar |
| "Pode gerar tudo" | O agente executa o lote sem parar a cada passo |

Formatos: veja a tabela em `fluxo-do-roteiro-ao-ar.md`. Se o conector não gerar 4:5, peça 3:4 ou 1:1 e recorte.

## Conferência de qualidade

A IA erra de forma que parece certa. Confira cada imagem e peça retoque pontual no que falhar:

- [ ] O produto é o produto de verdade (cor, embalagem, rótulo)?
- [ ] Todo texto está sem erro de ortografia e de acentuação em português?
- [ ] Preço, desconto, data e condições batem com a oferta real?
- [ ] Logo e cores corretos?
- [ ] Sem defeitos de mãos, rostos e objetos deformados?
- [ ] A chamada para ação combina com onde a pessoa converte (WhatsApp, loja física, site)?
- [ ] O layout inspira-se nas referências sem repetir o texto e os elementos delas?

Costuma bastar um ou dois retoques por imagem em vez de refazer o lote.

## Para Black Friday e outras datas

Use o mesmo pedido, trocando oferta e prazo. Gere os anúncios da **fase de construção** (marca, benefícios, prova) e
os da **fase de promoção** (oferta e urgência) em lotes separados. A skill `meta-ads` explica as fases e a verba.

## Em escala: base de referências, entrevista e envio à Meta

Fluxo descrito por um criador que gera dezenas de anúncios de uma vez:

1. **Base de referências**: reunir centenas de anúncios de exemplo em uma planilha ou banco de dados (imagem, texto,
   ramo, quanto tempo rodou). É o passo que a maioria pula, e ele melhora tudo.
2. **Seleção e entrevista**: pedir ao Claude para escolher os 50 que combinam com a oferta e fazer cerca de 20
   perguntas (oferta, público, estilo) antes de gerar.
3. **Geração em lote**: dezenas de anúncios de uma vez.
4. **Envio à conta de anúncios** pelo conector da Meta: indicar um anúncio que o usuário já montou na conta; o
   Claude copia as configurações dele e troca só o criativo e os textos.
5. **Teste**: o plano de teste e as regras de verba estão na skill `meta-ads`.

O custo relatado por esse criador foi de 10 a 50 centavos de dólar por imagem. Mesmo barato, **a prova está no
desempenho dos anúncios na conta**.
