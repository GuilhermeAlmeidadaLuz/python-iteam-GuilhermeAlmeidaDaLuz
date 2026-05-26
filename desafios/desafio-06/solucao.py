# Desafio 06 — Bio-Cadastro
# Aluno: Guilherme Almeida da Luz
# Data:  25/05/2026

# ── Escreva sua solução abaixo ──────────────────────────────────────────────

equipe = []
while True:
    entrada = str(input('Digite \'nome e cargo\' separado por vírgula ou \'sair\' (exemplo: nome, cargo): ').strip().title())
    if entrada.strip().lower() == 'sair':
        # percorra a lista e imprima: "Funcionário: {nome} | Cargo: {cargo}"
        for funcionario in equipe:
            print(f'Funcionário: {funcionario.get('nome')} | Cargo: {funcionario.get('cargo')}')
        break
    else:
        try:
            nome, cargo = entrada.split(',')
            equipe.append(
                {
                    'nome': nome.strip(),
                    'cargo': cargo.strip()
                }
            )
        except ValueError:
            print('Você precisa digitar um nome e um cargo separados por vírgula! Tente novamente...')
            continue
