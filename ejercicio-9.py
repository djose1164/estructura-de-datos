"""
La pizzería Dariannis Pizzas ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
ingredientes para cada tipo de pizza aparecen a continuación. A) Ingredientes vegetarianos:
Pimiento y tofu. b) Ingredientes no vegetarianos: Pepperoni, Jamón y Salmón. Escribir un
programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su
respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede
elegir un ingrediente además de la mozzarella y el tomate que están en todas las pizzas. Al
final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los
ingredientes que lleva
"""

DEFAULT_INGREDIENTS = "Mozzarella", "Tomate"


def menu():
    vegetarian_ingredientes = ["Pimiento", "Tofu"]
    non_vegetarian_ingredients = ["Pepperoni", "Jamón", "Salmón"]

    msg = """--- Bienvenid@ a la piezzeria Dariannis ---

- Que clase de pizza quiere pedir?
  1) Vegetariana.
  2) No vegetariana."""

    print(msg)
    opt = int(input("> "))
    if opt > 2:
        raise "Ingrese una opción validad."
    
    print("Cual de los siguientes ingredientes te gustaría elegir?")
    ingredients = vegetarian_ingredientes if opt == 1 else non_vegetarian_ingredients
    for i, ingredient in enumerate(ingredients, 1):
        print(f"  {i}) {ingredient}")

    opt2 = int(input("> "))
    return opt, ingredients[opt2-1]

def type_to_str(type: int) -> str:
    return "Vegetariana" if type == 1 else "No vegetariana"

def checkout(type_of_pizza: int, ingredient: str):
    print(f"Has pedido una pizza {type_to_str(type_of_pizza)} con los siguientes ingredients: ")
    for i in DEFAULT_INGREDIENTS:
        print(f"  -{i}")
    print(f"  -{ingredient}")
    
def main():
    checkout(*menu())

main()
