from decimal import Decimal, ROUND_HALF_UP

CASHBACK_BASE = Decimal("0.05")
THRESHOLD_PROMO_VALUE = Decimal("500.00")
VIP_BONUS_RATE = Decimal("0.10")

def calcular_cashback(
    valor_compra: float,
    percentual_desconto: float,
    tipo_cliente: str
) -> dict:
    valor_compra = Decimal(str(valor_compra))
    percentual_desconto = Decimal(str(percentual_desconto))

    # 1. Aplicar desconto
    desconto = valor_compra * (percentual_desconto / 100)
    valor_final = valor_compra - desconto

    # 2. Cashback base
    cashback = valor_final * CASHBACK_BASE

    # 3. Promoção Diretor Comercial (Dobra o cashback)
    if valor_final > THRESHOLD_PROMO_VALUE:
        cashback *= 2

    # 4. Bônus VIP (+10% sobre o montante acumulado até aqui)
    if tipo_cliente.strip().lower() == "vip":
        cashback += (cashback * VIP_BONUS_RATE)


    # O uso do ROUND_HALF_UP GARANTE QUE O SISTEMA SIGA UMA REGRA DE ARREDODAMENTO FIXA(comportamento diferente do round() do python)
    return {
        "valor_final": float(valor_final.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)),
        "valor_cashback": float(cashback.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
    }