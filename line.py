import math
def line():
    A= float(input("Ingrese el coeficiente A: "))
    B= float(input("Ingrese el coeficiente B: "))
    X1= float(input("Ingrese el coeficiente X1: "))
    X2= float(input("Ingrese el coeficiente X2: "))

    print (f"El coeficiente A de su ecuación de la recta es:{A}")
    print (f"El coeficiente B de su ecuación de la recta es:{B}")
    print (f"El coeficiente X1 de su ecuación de la recta es:{X1}")
    print (f"El coeficiente X2 de su ecuación de la recta es:{X2}")

    print("\nPara la siguiente ecuación:")
    print(f"\tY={A}X+{B}")

    Y1= A*X1+B
    Y2= A*X2+B
    print("Dados los siguientes puntos:")
    print (f"P1 ({X1};{Y1})")
    print(f"P2 ({X2};{Y2})")

    Distancia= math.sqrt((X2-X1)**2 + (Y2-Y1)**2)
    print(f"La distancia entre ellos es:{Distancia}")

line()
