# Explicação — Desafio 05 — Gerenciador de Compras

**Aluno:** _Guilherme Almeida da Luz_
**Data:** _24/05/2026_

---

## O que meu programa faz

_Coleta uma entrada de dados para colocar em uma lista de produtos para compra `enquanto` o usuário não digitar 'fim', após isso, exibe no terminal a lista de produtos numerada e o total de ítens, tudo isso de uma maneira formatada com `print` e `f-string`._

---

## Resposta à Pergunta Obrigatória

> Por que usamos uma **lista** e não uma **tupla** para essa lista de compras? O que mudaria no comportamento do programa se tentássemos usar tupla?

_Porque uma característica da lista é ser mutável, o que é imprescindível para continuar adicionando elementos nela enquanto o usuário quiser. Já as tuplas são imutáveis, uma vez criada não é possível deletar ou adicionar elementos. Se a abordagem fosse o uso de tupla, ocorreria erro na tentativa de adição._

---

## Dificuldades encontradas

_Pesquisei sobre formatação em f-strings, para que a numeração ficasse alinhada à direita, aprendi algo novo: para colocar uma variável nessa formatação preciso colocar outro par de chaves e a variável dentro `:>{ajuste_numeracao}`_
```python
ajuste_numeracao = len(f'{len(lista_de_produtos)}') # pega a quantidade de produtos, coloca dentro de uma string e recalcula o tamanho para saber a quantidade de dígitos utilizados.
for indice, produto in enumerate(lista_de_produtos):
    print(f'item {indice + 1 :>{ajuste_numeracao}} - {produto}')
```
