# @Kristianmartinezcolina  -> Programación en Python
#Como sacar el patrimonio en Contabilidad con Python y Manolo Sanchez del libro de la vida
"""Ejercicio
Manolo Sánchez, el talentoso torero y músico de El Libro de la Vida, ha decidido llevar un control de su patrimonio para asegurarse de que su futuro está bien administrado.

Datos
    Activo total (lo que posee): $10,000 MXN
    Pasivo total (lo que debe): $4,000 MXN

Pregunta: 
    ¿Cuál es el patrimonio neto de Manolo Sánchez?
"""
"""Formula
Patrimonio = Activo - Pasivo

Variables:
    Activo: Total de bienes y derechos.
    Pasivo: Deudas y obligaciones financieras (lo que debe).
    Patrimonio Neto: Lo que realmente le pertenece después de pagar sus deudas.
"""

import locale 
from decimal import Decimal 

locale.setlocale(locale.LC_ALL, 'es_MX.UTF-8')

def formato_mx(valor):
    return f"${valor:,.4f} MXN"

def calcular_patrimonio():
    try: 
        activos = Decimal(input("Dame los activos: "))
        pasivos = Decimal(input("Dame los pasivos: "))

        patrimonio = activos - pasivos

        print("Resumen del patrimonio: ")
        print(f"Activos: {formato_mx(activos)}")
        print(f"Pasivos: {formato_mx(pasivos)}")
        print(f"Total del patrimonio:{formato_mx(patrimonio)}")
    except Exception as error: 
        print(f"Hay un error {error}")

calcular_patrimonio()


# @Kristianmartinezcolina  -> Programación en Python