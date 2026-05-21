# Explicação — Desafio 02 — Calculadora de IMC

**Aluno:** _Guilherme Almeida da Luz_
**Data:** _21/05/2026_

---

## O que meu programa faz

_Coleta dados do usuário (`nome_do_usuario, peso_do_usuario, altura_do_usuario`), em seguida calcula o `valor_do_imc` usando `peso_do_usuario / (altura_do_usuario ** 2)`. Por fim, exibe no terminal o nome, com valor do imc dentro de uma f-string `print(f'Olá {nome_do_usuario}, seu IMC é {valor_imc:.2f}')`_

---

## Resposta à Pergunta Obrigatória

> Por que é necessário usar `float()` ao capturar peso e altura com `input()`? O que aconteceria se usássemos `int()` para a altura `1.75`?

_Porque é preciso fazer casting ou conversão da entrada de dado capturada pelo teclado do usuário que é do tipo `str` por padrão dentro do `input`. Para que seja possível fazer cálculo usando os operadores matemáticos, visto que só funciona com tipos númericos `int` e `float`, a não ser que fosse uma concatenação de strings com o operador **`(+)`** que o interpretador python aceita. Além disso, se usasse a conversão para `int` de um valor decimal ou `float` em python, ocorreria o truncamento e seria considerado somente a parte inteira antes do ponto flutuante/decimal (exemplo: `int(1.75)` transformaria o valor em `1`)_

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
