def line():
    print("TO DO")
    import math
    
    CofA= float(input("Ingrese el coeficiente A: "))
    CofB= float(input("Ingrese el coeficiente B: "))
    CofX1= float(input("Ingrese el coeficiente X1: "))
    CofX2= float(input("Ingrese el coeficiente X2: "))
    
    print (f"El coeficiente A de su ecuación de la recta es:{CofA}")
    print (f"El coeficiente B de su ecuación de la recta es:{CofB}")
    print (f"El coeficiente X1 de su ecuación de la recta es:{CofX1}")
    print (f"El coeficiente X2 de su ecuación de la recta es:{CofX2}")
    
    print("Para la siguiente ecuación:")
    print(f"Y={CofA}X+{CofB}")
    
    Y1= CofA*CofX1+CofB
    Y2= CofA*CofX2+CofB
    print("Dados los siguientes puntos:")
    print (f"P1 ({CofX1};{Y1})")
    print(f"P2 ({CofX2};{Y2})")
    
    Distancia= math.sqrt((CofX2-CofX1)**2 + (Y2-Y1)**2)
    print(f"La distancia entre ellos es:{Distancia}")
line()
