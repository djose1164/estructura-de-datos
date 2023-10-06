"""
Para tributar (pagar impuesto DGII) un determinado impuesto se debe ser mayor de 18 años
y tener unos ingresos iguales o superiores a 35,000 mensuales. Escribir un programa que
pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario
tiene que tributar o no.
"""

age = int(input("Ingrese su edad: "))
if age < 18:
    print("No tiene que tributar.")
    exit()

salary = int(input("Ingrese su salario: "))
if salary < 35_000:
    print("No tiene que tributar.")
else:
    print("Si tiene que tributar.")