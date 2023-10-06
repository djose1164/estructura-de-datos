"""
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas.
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
paquete así que deben calcular el peso de los payasos y muñecas que saldrán en
cada paquete a demanda. Cada payaso pesa 112 LB y cada muñeca 75 LB. Escribir un
programa que lea el número de payasos y muñecas vendidos en el último pedido y
calcule el peso total del paquete que será enviado.
"""

CLOWN_WEIGHT: int = 112
DOLL_WEIGHT: int = 75

def ask_for_toys() -> tuple[int, int]:
    clowns = int(input("Ingrese el numero de payasos en este pedido: "))
    dolls = int(input("Ingrese el numero de muñecas en este pedido: "))
    return clowns, dolls

def calculate_order_weight(clowns: int, dolls: int) -> int:
    return CLOWN_WEIGHT*clowns + DOLL_WEIGHT*dolls

def main():
    while True:
        print(f"El tamaño total del pedido es: {calculate_order_weight(*ask_for_toys())}")
        opt = input("Desea continuar con otro pedido? [y/n]: ")
        if opt.lower() == "n":
            break

main()
