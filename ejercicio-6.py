"""
Escribir un programa que almacene la cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y
Minúsculas.
"""

PASSWORD = "hola"
password = input("Ingrese la contraseña: ")

if password.lower() == PASSWORD:
    print("La contraseña introducida coinciden.")
else:
    print("La contraseña introducida no coinciden.")
