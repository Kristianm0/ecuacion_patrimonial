# @Kristianmartinezcolina  -> Programación en Python
#Como sacar los pasivos en Contabilidad con Python y el Chavo del 8
"""Ejercicio
El Chavo del 8 ha recibido algunas donaciones y posee ciertos bienes, pero también tiene deudas con Doña Florinda y el Señor Barriga.

Datos:
    Patrimonio Neto: $500 MXN
    Activo Total: $1,500 MXN

Pregunta: 
    ¿Cuánto es el Pasivo de El Chavo 8?
"""
"""Formula
Pasivos = Activos - Patrimonio

Variables:
    Activo: Total de bienes y derechos de El Chavo 8.
    Pasivo: Deudas y obligaciones financieras (lo que debe).
    Patrimonio Neto: Lo que realmente le pertenece después de pagar sus deudas.
"""

import locale 
from decimal import Decimal

locale.setlocale(locale.LC_ALL, 'es_MX.UTF-8')

def formato_mx(valor):
    return f"${valor:,.2f} MXN"

def calcular_pasivos():
    try:
        activos = Decimal(input("La cantidad de activos: "))
        patrimonio = Decimal(input("Dame el patrimonio: "))

        pasivos = activos - patrimonio

        print("Resumen de los pasivos del chavo del 8: ")
        print(f"Activos: {formato_mx(activos)}")
        print(f"Patrimonio Neto: {formato_mx(patrimonio)}")
        print(f"Los Pasivos total: : {formato_mx(pasivos)}")

    except Exception as error:
        print(f"Hay un error {error}")

calcular_pasivos()

# @Kristianmartinezcolina  -> Programación en Python