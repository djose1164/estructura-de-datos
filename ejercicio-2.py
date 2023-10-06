"""
2- Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión.
"""

print("Ingrese la cantidad a invertir, el interés anual, y el número de años. \
      \nEjemplo: 50000 6.7 15")

parameters = [float(i) for i in input("> ").split()]
inversion, interest, years = parameters

result = inversion*(1+interest/100)*years

print(f"El capital obtenido en la inversion es de {result}")