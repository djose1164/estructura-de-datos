"""
Una panadería vende barras de pan a 3.49$ cada una. El pan que no es el día tiene
un descuento del 60%. Escribir un programa que comience leyendo el número de
barras vendidas que no son del día. Después el programa debe mostrar el precio
habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste
final total.
"""

NORMAL_COST = 3.49
COST_WITH_DISCOUNT = NORMAL_COST*.6

cooked_yesterday = int(input("Ingrese las barras vendidas que no son del dia: "))
print(f"-- El precio normal de una barra de pan es de ${NORMAL_COST}")
print(f"-- Las barras que no son frescas reciben un descuento del 60%: ${COST_WITH_DISCOUNT:.2f}")
print(f"-- El total a pagar asciende a ${cooked_yesterday*COST_WITH_DISCOUNT:.2f}")
