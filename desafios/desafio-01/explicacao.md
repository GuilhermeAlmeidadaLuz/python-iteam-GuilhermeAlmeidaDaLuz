# Explicação — Desafio 01

**Aluno:** _Guilherme Almeida da Luz_  
**Data:** _18/05/2026_

---

## O que meu programa faz

_(Descreva em suas palavras o que cada parte do código faz. Não copie o enunciado — explique como você pensou na solução.)
Primeiro coletei os dados requeridos pelo exercício (`nome, ano_de_nascimento, hobbies, ano_atual`),
depois fiz o cálculo `idade = ano_atual - ano_de_nascimento`.
Por fim, exibi na tela com o comando `print(f"Olá, {nome}.\nVocê tem {idade} ano(s) e gosta de {hobbies}")`_

---

## Resposta à Pergunta Obrigatória

> Por que é necessário converter o resultado do `input()` antes de calcular a idade? O que acontece se não converter?

_Porque o `input()` por padrão recebe um valor como `string` (cadeia de caracteres) e a data de nascimento coletada do usuário precisa ser do tipo `int` (inteiro) para efetuar o cálculo de subtração do ano atual (que também deve ser `int`) pela data de nascimento, para enfim obter a idade. No fim, só é possível fazer a operação matemática de subtração se ambas as variáveis ou valores forem do tipo `int`, caso contrário, ocorrerá erro de operandos não suportados para `int` e `str`. Além disso, se for tentar converter em `int` algo que não seja número, ocorrerá erro antes de chegar na operção de subtração. Exemplo:_
```python
# o dado obtido no input é do tipo str, mas com int é feita uma conversão antes de atribuir em data_de_nascimento
ano_de_nascimento = int(input("Digite seu ano de nascimento: ")) 
```

---

## Dificuldades encontradas

_(Opcional: o que foi difícil? O que você pesquisou para resolver?)_
