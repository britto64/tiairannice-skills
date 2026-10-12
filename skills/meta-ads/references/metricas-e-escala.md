# Métricas e escala

Estudado em out/2026. Use para decidir quanto gastar, quando aumentar a verba e como diagnosticar uma conta. Os
números de referência dos criadores são de e-commerce de fora do Brasil e são relatos sem fonte: servem como ordem
de grandeza, não como meta.

## Além do ROAS: quanto vale cada cliente

Quem olha só o retorno imediato (ROAS) fica limitado. Marcas que escalam olham também:

| Métrica | O que mostra |
|---|---|
| **CAC** (custo para adquirir um cliente) | Quanto se paga para conquistar um comprador |
| **LTV** (valor do cliente ao longo do tempo) | Quanto ele deixa de receita (e de margem) em toda a relação |
| **LTV : CAC** | Quantas vezes o cliente retorna o que custou. Os criadores citam categorias de recompra, como suplementos e cuidados com a pele, com algo entre 3x e 6x como referência saudável (relato deles) |
| **Ticket médio** | Quanto cada compra rende; kits e combos aumentam |
| **Recompra e assinatura** | Quantos clientes voltam; recorrência torna o cliente mais valioso |

Lógica: **se cada cliente vale mais, você pode gastar mais para conquistá-lo**, e é isso que permite escalar
quando os concorrentes estão limitados pelo ROAS imediato.

## Ponto de equilíbrio do ROAS (conta nossa)

```
receita da venda       = preço já com o desconto da promoção
contribuição por venda = receita da venda - custos variáveis (produto, embalagem, entrega, taxas)
ROAS de equilíbrio     = receita da venda ÷ contribuição por venda
```

Exemplo: preço de tabela R$ 100; na promoção, 15% de desconto, então a receita da venda é R$ 85; custos variáveis
R$ 55. Contribuição = 85 - 55 = R$ 30. ROAS de equilíbrio = 85 ÷ 30 ≈ **2,8**. Fora da promoção: receita R$ 100,
contribuição R$ 45, equilíbrio = 100 ÷ 45 ≈ **2,2**. Por isso a meta de ROAS de uma data de promoção não pode ser
a mesma do resto do ano: o mesmo gasto precisa trazer mais receita para não dar prejuízo.

Meta de lucro: quem quer lucro direto na campanha trabalha com um ROAS acima do equilíbrio; quem investe em
aquisição aceita ficar perto do equilíbrio (ou abaixo) e cobra o retorno pela recompra (LTV).

## Regras de escala

1. **Aumente o orçamento apenas quando a meta estiver sendo cumprida**, e a cada 2 dias ou mais (não a cada hora).
2. **Julgue por uma janela longa** quando estiver investindo (por exemplo, 60 dias). A queda de ROAS de uma fase
   de construção de funil não é fracasso se o retorno vem depois.
3. **Verifique nos dois lugares:** no gerenciador de anúncios e no sistema de vendas da loja (as duas fontes
   podem divergir).
4. **Escale horizontalmente** (mais campanhas, mais criativos, mais públicos) além de subir o orçamento.
5. **Renove criativo** antes de cansar (ver `volume-e-variacoes.md`).
6. **Saiba de onde vêm os que fecham e os que não fecham** (atribuição): sem isso não dá para saber o que repetir.

## Diagnóstico por métrica (heurísticas gerais, nossas)

| O que você vê | Hipótese principal | Onde mexer primeiro |
|---|---|---|
| CTR baixo | Gancho e imagem não param o dedo | Criativo: gancho, persona, formato |
| CTR bom, poucas vendas | Página, oferta ou preço não convencem | Página/WhatsApp, prova, garantia |
| Custo por resultado subindo aos poucos | Fadiga ou saturação do público | Criativos novos, variações dos vencedores |
| ROAS bom, vendas baixas | Verba limitada ou público pequeno | Aumentar verba com regra; ampliar público |
| Muita venda, margem apertada | Desconto alto ou custo de entrega | Oferta, kit, ticket médio, frete |
| Cliente compra uma vez | Pós-venda e recorrência fracos | Relacionamento, recompra, assinatura |

## Cuidados

- Não prometa ao usuário um ROAS ou um CAC: depende do nicho, do preço, da margem e da execução.
- Peça os dados reais da conta (verba, vendas, margem, histórico) antes de recomendar metas; se houver um conector
  com a conta de anúncios, use-o.
- Aumentos agressivos de orçamento só fazem sentido com histórico e retorno comprovado; para contas pequenas, vá
  devagar.
