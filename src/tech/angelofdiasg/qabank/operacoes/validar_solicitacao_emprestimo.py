# Crie uma função chamada validar_solicitacao_emprestimo que valide se uma solicitação de empréstimo pode ser aprovada no QaBank.

# Regra de negócio:

# O cliente deve ter pelo menos 18 anos.
# O score de crédito deve ser maior ou igual a 650.
# O salário mensal deve ser maior que zero.
# O valor solicitado deve ser maior que zero.
# O valor solicitado não pode ultrapassar 10 vezes o salário mensal.
# A dívida mensal não pode comprometer mais de 40% da renda do cliente.
# Se o cliente for menor de idade, a função deve lançar exceção.
# Se qualquer dado obrigatório estiver ausente, nulo ou em formato inválido, a função deve tratar como erro de entrada.
# Se o score for insuficiente, o salário for inválido, o valor do empréstimo for inválido, ou a dívida comprometer mais de 40% da renda, o resultado deve ser "Recusado".
# Se todas as condições forem atendidas, o resultado deve ser "Aprovado".


# Critérios de aceitação:

# Menor de 18 anos → exceção
# Score abaixo de 650 → "Recusado"
# Salário menor ou igual a zero → "Recusado"
# Valor do empréstimo menor ou igual a zero → "Recusado"
# Valor do empréstimo acima de 10x o salário → "Recusado"
# Dívida mensal acima de 40% da renda → "Recusado"
# Dados inválidos ou ausentes → erro de validação
# Tudo válido → "Aprovado"


def validar_solicitacao_emprestimo(
    idade,
    score_credito,
    salario_mensal,
    valor_solicitado,
    divida_mensal
):
    """
    Valida se uma solicitação de empréstimo pode ser aprovada no QaBank.

    Regras de negócio:
    - Cliente deve ter pelo menos 18 anos.
    - Score deve ser maior ou igual a 650.
    - Salário mensal deve ser maior que zero.
    - Valor solicitado deve ser maior que zero.
    - Valor solicitado não pode ultrapassar 10x o salário.
    - Dívida mensal não pode ultrapassar 40% da renda.
    - Menor de idade gera exceção.
    - Dados inválidos geram erro de validação.
    """

    # Validação dos dados de entrada
    if (
        idade is None
        or score_credito is None
        or salario_mensal is None
        or valor_solicitado is None
        or divida_mensal is None
    ):
        raise ValueError("Dados obrigatórios ausentes")

    # Validação do tipo dos dados
    if not all(
        isinstance(valor, (int, float))
        for valor in [
            idade,
            score_credito,
            salario_mensal,
            valor_solicitado,
            divida_mensal
        ]
    ):
        raise ValueError("Dados inválidos")

    # Menor de idade
    if idade < 18:
        raise ValueError("Menor de idade não permitido")

    # Score insuficiente
    if score_credito < 650:
        return "Recusado"

    # Salário inválido
    if salario_mensal <= 0:
        return "Recusado"

    # Valor do empréstimo inválido
    if valor_solicitado <= 0:
        return "Recusado"

    # Empréstimo acima de 10x o salário
    if valor_solicitado > salario_mensal * 10:
        return "Recusado"

    # Dívida acima de 40% da renda
    if divida_mensal > salario_mensal * 0.40:
        return "Recusado"

    return "Aprovado"
