# Lista 01 — Questão 03: Ficha de Cadastro
# Aluno: Guilherme Almeida da Luz
# Data:  22/05/2026

# ── Enunciado ───────────────────────────────────────────────────────────────
# Solicite: nome completo, CPF (str), ano de nascimento (int), altura (float).
# O programa deve:
#   1. Calcular e exibir a idade em 2026.
#   2. Exibir todos os dados com f-string e tipos corretos.
#   3. Tratar com try/except o caso em que o ano não seja um número.
# Explique em comentário: por que float para altura e não int?

# ── Sua solução abaixo ──────────────────────────────────────────────────────

try:
    # entrada de dados:
    nome_completo = ''
    nome_invalido = True
    while nome_invalido:
        nome_completo = str(input('Digite seu nome completo: ')).title()
        if (''.join(nome_completo.split(' ')) . isalpha()) and (len(nome_completo) > 2): # verifica se o nome sem espaços é composto só por letras alfabéticas E maior que 2 letras
            nome_invalido = False
        else:
            print(f'Digite um nome válido! Seu nome não pode ter só {len(nome_completo)} letra(s) ou ter dígitos que não sejam letras...')
        
    cpf = str(input('Digite seu CPF (exemplo: xxx.xxx.xxx-xx): '))
    ano_de_nascimento = int(input('Digite seu ano de nascimento (exemplo: 2000): '))
    altura = float(input('Digite sua altura em metros (exemplo: 1.75): '))  # float para altura, pois por padrão é capturado em metros

    # processamento da idade:
    idade = 2026 - ano_de_nascimento

    # saída no terminal:
    print(f'\nNome Completo: {nome_completo}\n'
        f'CPF: {cpf}\n'
        f'altura: {altura}\n'
        f'idade: ~ {idade} ano(s)\n')

except ValueError as e:
    print('\nTipo de Erro:', type(e), '|', 'Mensagem: você inseriu um valor não permitido no teclado, observe com detalhes a(s) linha(s) do Traceback abaixo e procure por \'ValueError\' para entender\n')
    raise