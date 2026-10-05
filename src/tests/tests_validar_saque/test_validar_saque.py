import pytest

from tech.angelofdiasg.qabank.operacoes.validar_saque import validar_saque


@pytest.fixture
def saque_base():
    """Fornece um pedido válido para ser adaptado em cada teste."""
    return {
        "valor": 300,
        "conta": {
            "tipo": "corrente",
            "saldo": 1200,
            "total_sacado_hoje": 400,
        },
    }


@pytest.mark.parametrize(
    "tipo, valor, total_sacado_hoje, status_esperado, motivo_esperado",
    [
        pytest.param(
            "corrente", 500, 1500, "Aprovado", "Saque autorizado",
            id="corrente-no-limite-diario",
        ),
        pytest.param(
            "corrente", 501, 1500, "Recusado", "Limite diário de saque excedido",
            id="corrente-acima-do-limite-diario",
        ),
        pytest.param(
            "poupanca", 300, 700, "Aprovado", "Saque autorizado",
            id="poupanca-no-limite-diario",
        ),
        pytest.param(
            "poupanca", 301, 700, "Recusado", "Limite diário de saque excedido",
            id="poupanca-acima-do-limite-diario",
        ),
    ],
)
@pytest.mark.skip(reason="Atividade: complete a análise e remova o skip")
def test_validar_saque_por_tipo_e_limite_diario(
    saque_base,
    tipo,
    valor,
    total_sacado_hoje,
    status_esperado,
    motivo_esperado,
):
    saque_base["conta"]["tipo"] = tipo
    saque_base["valor"] = valor
    saque_base["conta"]["total_sacado_hoje"] = total_sacado_hoje

    resultado = validar_saque(saque_base)

    assert resultado["status"] == status_esperado
    assert resultado["motivo"] == motivo_esperado


@pytest.mark.skip(reason="Atividade: acrescente casos e remova o skip")
def test_dados_invalidos_lancam_value_error(saque_base):
    with pytest.raises(ValueError, match="Dados do saque inválidos"):
        validar_saque(None)