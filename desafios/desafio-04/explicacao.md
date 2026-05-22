# Explicação — Desafio 04 — Tabuada Personalizada

**Aluno:** _Guilherme Almeida da Luz_
**Data:** _21/05/2026_

---

## O que meu programa faz

_Executa um loop infinito com `while True`, que espera um número inteiro como entrada do teclado que esteja entre 0 e 10 e é interrompido `se` digitar `0`. Caso o número esteja fora desse intervalo, é capturado por um `elif` que salta para a próxima execução do loop com o comando `continue`, recomeçando o processo de coleta do número. `Se não` cair em nenhuma das duas primeiras condições, utiliza um loop ou laço `for` de 1 até 10, incrementando de 1 em 1, onde para cada execução calcula a tabuada do `numero_escolhido` e imprime na tela com a formatação comum de uma tabuada_

---

## Resposta à Pergunta Obrigatória

> Para esse exercício, por que `for` com `range()` é preferível ao `while`? Em que cenário o `while` seria a escolha certa?

_Porque se entende que uma tabuada tem um fim desejado, nesse caso o número escolhido será multiplicado por cada número de 1 até 10, valores de uma tabuada padrão, por isso a escolha do `for`. Quando precisamos executar várias vezes até que uma condição de parada seja atendida, ou seja, não sabemos até quando executar de maneira fixa, optamos por `while`_

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
