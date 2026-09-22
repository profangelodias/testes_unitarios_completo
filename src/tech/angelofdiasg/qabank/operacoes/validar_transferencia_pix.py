
def validar_transferencia_pix(
    saldo_conta,
    valor_transferencia,
    conta_destino,
    limite_diario,
    horario_transferencia
):
    """
    Regra de negócio do QaBank:

    - O saldo deve ser suficiente para realizar a transferência.
    - O valor da transferência deve ser maior que zero.
    - A conta de destino deve ser informada.
    - O valor não pode ultrapassar o limite diário.
    - Transferências só podem ser realizadas em horário comercial.
    """

    # Verifica se existe saldo suficiente
    if saldo_conta < valor_transferencia:
        return "Recusado"

    # Verifica se o valor é válido
    if valor_transferencia <= 0:
        return "Recusado"

    # Verifica o limite diário
    if valor_transferencia > limite_diario:
        return "Recusado"

    # Brecha intencional:
    # A validação da conta de destino foi esquecida.
    # A validação do horário também foi esquecida.

    return "Aprovado"

