# @Kristianmartinezcolina  -> Programación en Python
#Ejercicio de Ecuación Patrimonial con Ernesto de la Cruz
"""Ejercicio
Problema:
Ernesto de la Cruz ha acumulado riquezas gracias a sus regalías musicales y su carrera en el cine. 
Sin embargo, también tiene deudas que debe pagar.

Datos:
Patrimonio Neto: $4,000,000 MXN  
Pasivo (deudas): $1,500,000 MXN  

Pregunta:
¿Cuánto es el Activo total de Ernesto de la Cruz?
"""
"""Fórmula básica de contabilidad:
Activo = Pasivo + Patrimonio Neto
----
📌 Variables:
    - Activo (A): Total de bienes y derechos de Ernesto (dinero, regalías, propiedades, etc.).
    - Pasivo (P): Deudas y obligaciones financieras (lo que debe).
    - Patrimonio Neto (PN): Lo que realmente le pertenece después de pagar sus deudas.
"""

import locale 
from decimal import Decimal

locale.setlocale(locale.LC_ALL, 'es_MX.UTF-8')

def calcular_activos():
    try: 
        pasivo = Decimal(input("Dame el pasivo: "))
        patrimonio = Decimal(input("Dame el patrimonio: "))

        activo = pasivo + patrimonio

        def formato_mx(valor):
            return f"${valor:,.2f} MXN"
        
        # Mostrar resultados
        print("Resumen de los Activos de Ernesto de la Cruz")
        print(f"📜 Pasivo (deudas): {formato_mx(pasivo)}")
        print(f"🤑 Patrimonio Neto: {formato_mx(patrimonio)}")
        print(f"Activos total de Ernesto: {formato_mx(activo)}")

    except Exception as error:
        print(f"Hay un error {error}")

calcular_activos()

# @Kristianmartinezcolina  -> Programación en Python