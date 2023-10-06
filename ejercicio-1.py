"""
1- Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
calcule el índice de masa corporal y lo almacene en una variable, y muestre por
pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el
índice de masa corporal calculado redondeado con dos decimales.
"""

weight: float = float(input("Ingrese su peso en kilos (kg): "))
height: float = float(input("Ingrese su estatura en metros (m):"))

imc: float = weight/(height**2)

print(f"Tu indice de masa corporal es {imc}.")