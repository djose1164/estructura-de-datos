"""
En la empresa Mike & Asociados SRL, sus empleados son evaluados al final de cada año
(Evaluación de desempeño). Los puntos que pueden obtener en la evaluación comienzan en
0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden
conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre
las cifras mencionadas. A continuación, se muestra una tabla con los niveles
correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de
2.400$ USD multiplicada por la puntuación del nivel. Escribir un programa que lea la
puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero
que recibirá el usuario
"""

SALARY_PER_LEVEL = 2_400

def get_salary() -> float:
    points = float(input("Ingrese los puntos del empleado: "))
    if points < .9 and (points*10)%2 == 0:
        return SALARY_PER_LEVEL * points
    elif points < 1 and (points*100)%2 == 0:
        return SALARY_PER_LEVEL * points
    elif points%2 == 0:
        return SALARY_PER_LEVEL * points

salary = get_salary()
if salary is not None:
    print(f"El empleado por su rendimiento ha conseguido un salario de: ${salary:.2f}")
else:
    print("Ingrese unos puntos que sean validos.")
