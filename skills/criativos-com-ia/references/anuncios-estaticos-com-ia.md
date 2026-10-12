# Anúncios estáticos com IA

Estudado em out/2026. Use quando o usuário quer gerar vários anúncios de imagem de uma vez (produto, promoção,
Black Friday), partindo de referências, e eventualmente enviá-los à conta de anúncios. As ferramentas e os preços
mudam rápido; o método abaixo é o que permanece. Resultados citados pelos criadores (como "mais de 30 mil dólares
com imagens geradas por IA") são relatos sem verificação.

## A receita em uma frase

Um pedido bem montado, com **marca, oferta exata, referências de layout, persona e formato**, devolve de 5 a 10
anúncios sólidos em poucos minutos, usando o Claude com um conector de geração de imagem. O trabalho humano passa a
ser **briefar bem e revisar**, não desenhar.

## Modelo de pedido (adapte e cole no Claude)

```
Crie [N] anúncios para [marca / promoção], usando [conector de imagem].

Marca: site [endereço]. Use as cores e o logo da marca e a foto EXATA do produto que está no site.
Oferta: [texto exato, ex.: "30% de desconto em todo o site até 30/11"]. Não invente preços nem condições.
Pessoa e situação: [persona e a dor ou situação que o produto resolve].
Ângulos: proponha ângulos e escolha os com maior chance de converter, dizendo por quê.
Referências: anexei [3 a 4] anúncios de marcas do mesmo ramo, só como inspiração de layout e de estilo.
  Não copie textos, elementos de marca nem imagens deles.
Mistura: metade com a oferta no título e o botão de chamada na parte de baixo, perto do produto;
  metade com um título criativo sobre o produto e a oferta em segundo plano.
Formato: [4:5 para feed / 9:16 para stories e reels]. Idioma: português do Brasil, com acentos corretos.
Pode gerar tudo. Antes, faça no máximo 5 perguntas se faltar algo essencial. Ao final, devolva uma tabela com
persona, ângulo e título de cada anúncio.
```

Por que cada parte importa:

| Parte | Motivo |
|---|---|
| Foto exata do produto | Evita que a IA invente um produto parecido (perde a fidelidade e a credibilidade) |
| Oferta em texto exato | Evita preço, prazo ou condição inventados |
| Referências de layout | Dão um ponto de partida de design que já funciona no ramo |
| Persona e ângulo | Sem isso o anúncio fica genérico (ver `criativos-que-performam` na skill `meta-ads`) |
| Dois tipos de anúncio | Permite testar oferta pura contra título criativo |
| Perguntas antes de gerar | O agente se alinha em vez de adivinhar |
| "Pode gerar tudo" | Evita pedidos de autorização a cada passo |

Tamanhos usuais (confirme as medidas atuais da Meta): feed em 4:5 (1080 × 1350) e stories e reels em 9:16
(1080 × 1920).

## Revisão obrigatória antes de usar

A IA erra de forma que parece certa. Confira cada imagem:

- [ ] O produto é o produto de verdade (cor, embalagem, rótulo)?
- [ ] Todo texto está sem erro de ortografia e de acentuação em português?
- [ ] Preço, desconto, data e condições batem com a oferta real?
- [ ] Logo e cores corretos?
- [ ] Sem defeitos de mãos, rostos, objetos deformados?
- [ ] A promessa respeita as políticas da plataforma e do setor (saúde, antes e depois, etc.)?
- [ ] A chamada para ação combina com onde a pessoa converte (WhatsApp, loja física, site)?
- [ ] Nada copiado das referências (texto, marca, personagem)?

Se alguma imagem falhar, peça ajustes pontuais em vez de refazer tudo; costuma bastar um ou dois retoques.

## Para Black Friday e outras datas

Use o mesmo pedido, trocando oferta e prazo. Gere os anúncios da **fase de construção** (marca, benefícios, prova)
e os da **fase de promoção** (oferta e urgência) em lotes separados. A skill `meta-ads` explica as fases e a
verba.

## Em escala: referências, entrevista e envio à conta

Um criador descreve um fluxo mais completo, que só vale com cuidado:

1. **Base de referências**: reunir centenas de anúncios de exemplo em uma planilha ou banco de dados (imagem, texto,
   ramo, quanto tempo rodou). Este é o passo que a maioria pula, e ele melhora tudo.
2. **Seleção e entrevista**: pedir ao Claude para escolher os 50 que combinam com a sua oferta e fazer cerca de 20
   perguntas (oferta, público, estilo) antes de gerar.
3. **Geração em lote**: dezenas de anúncios de uma vez.
4. **Envio à conta de anúncios**: ligar a conta por um conector e mandar subir os criativos, **clonando as
   configurações de um anúncio que você mesmo montou à mão**, trocando só o criativo.

**Cuidados** (nossos, importantes): dar a um agente acesso de escrita à conta de anúncios pode gastar dinheiro.

- Peça para criar tudo **pausado**, revise e ative você mesmo.
- Defina limite de gasto na conta e nas campanhas.
- Não cole chaves de acesso em conversas; guarde-as em local seguro e revogue as que vazarem.
- Teste primeiro com poucos anúncios.
- Confira os direitos das referências: usar anúncio de terceiros como inspiração de layout é diferente de copiá-lo.

Custo relatado por um criador: de 10 a 50 centavos de dólar por imagem. Mesmo barato, **o teste real é o desempenho
na conta**, e o plano de teste está na skill `meta-ads`.
