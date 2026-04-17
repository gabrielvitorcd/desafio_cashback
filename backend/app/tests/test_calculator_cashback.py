import pytest
from decimal import Decimal
from app.service.service import calcular_cashback

@pytest.mark.parametrize("valor, desconto, tipo, esperado_final, esperado_cashback", [
    # 1. Caso Base: R$ 100, 0% desc, Normal -> Cashback R$ 5.00
    (100.0, 0.0, "normal", 100.0, 5.0),
    
    # 2. Arredondamento ROUND_HALF_UP: R$ 10.01 * 5% = 0.5005 -> Deve subir para 0.50
    # Nota: 10.01 * 0.05 = 0.5005. O HALF_UP arredonda 0.0005 para cima.
    (10.01, 0.0, "normal", 10.01, 0.5),

    # 3. Limite da Promoção (Exatos R$ 500 não dobra)
    (500.0, 0.0, "normal", 500.0, 25.0),

    # 4. Acima do Limite (R$ 500.01 dobra)
    # 500.01 * 0.05 = 25.0005 -> Dobra -> 50.001 -> Arredonda 50.00
    (500.01, 0.0, "normal", 500.01, 50.0),

    # 5. Cliente VIP sem promoção
    # 100 * 0.05 = 5.0 -> + 10% = 5.50
    (100.0, 0.0, "VIP", 100.0, 5.5),

    # 6. Cliente VIP com promoção (> 500)
    # 1000 * 0.05 = 50 -> Dobra = 100 -> + 10% VIP = 110.0
    (1000.0, 0.0, "vip", 1000.0, 110.0),

    # 7. Com Desconto que joga o valor para baixo do limite
    # 1000 - 60% = 400 (não dobra) -> 400 * 0.05 = 20.0
    (1000.0, 60.0, "normal", 400.0, 20.0),
    
    # 8. Teste de sanitização de string (Espaços e Case)
    (100.0, 0.0, "  vIp  ", 100.0, 5.5),
])
def test_calcular_cashback_cenarios(valor, desconto, tipo, esperado_final, esperado_cashback):
    resultado = calcular_cashback(valor, desconto, tipo)
    
    assert resultado["valor_final"] == esperado_final
    assert resultado["valor_cashback"] == esperado_cashback

def test_calcular_cashback_valor_zero():
    resultado = calcular_cashback(0.0, 0.0, "normal")
    assert resultado["valor_cashback"] == 0.0