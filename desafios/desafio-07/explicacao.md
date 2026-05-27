# Explicação — Desafio 07 — Bio-Calculadora

**Aluno:** _Guilherme Almeida da Luz_
**Data:** _26/05/2026_

---

## O que meu programa faz

_Detro do arquivo/módulo `solucao.py` o código coleta o cálculo desejado e atráves de uma
estrutura `match/case` faz o controle codicional, determinando o bloco de código a ser executado que coletará os dados necessários para a operação, em seguida, uma das funções do outro arquivo/módulo que foi importado no início do código é chamada com os valores coletados da entrada do teclado como argumentos, a função retorna um valor que é atribuído a variável resultado e exibido na tela. O outro arquivo/módulo de nome `funcoes_mat.py` conta com 3 funções para cálculo: `area_do_circulo, volume_da_esfera, hipotenusa`._

---

## Resposta à Pergunta Obrigatória

> Por que separar as funções em um arquivo diferente do `solucao.py`? O que muda no projeto quando você tem 50 funções em vez de 3?

_Porque isso facilita a manutenção e o isolamento de responsabilidades à medida que o sistema cresce. É mais fácil analisar arquivos separados com poucas linhas do que um arquivo com muitas linhas. Se o projeto tiver 50 funções, é preciso organizar por contexto e pastas para que nenhum arquivo fique tão grande que seja difícil dar manutenção._

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
