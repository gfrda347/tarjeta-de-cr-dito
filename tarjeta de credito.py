def calcular_pago_mensual(monto_compra, tasa_interes_anual, numero_pagos):
    tasa_interes_mensual = (tasa_interes_anual / 12) / 100
    
    pago_mensual = (monto_compra * tasa_interes_mensual * (1 + tasa_interes_mensual)**numero_pagos) / \
                ((1 + tasa_interes_mensual)**numero_pagos - 1)
    
    return pago_mensual

monto_compra = float(input("Ingrese el monto de la compra: "))
tasa_interes_anual = float(input("Ingrese la tasa de interés anual (%): "))
numero_pagos = int(input("Ingrese el número de pagos (meses): "))

pago_mensual = calcular_pago_mensual(monto_compra, tasa_interes_anual, numero_pagos)
print(f"El pago mensual será de: {round(pago_mensual, 2)}")
