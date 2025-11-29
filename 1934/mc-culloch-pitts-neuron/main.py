"""
Proyecto: Neurona de McCulloch-Pitts (1934)
"""

def main():
    """Función principal del programa."""
    print("Bienvenido al proyecto de la Neurona de McCulloch-Pitts")
    print("Este es el primer modelo matemático de neurona artificial (1943)")


def neuronNOT(d,t):

    w = -2 # Peso de la neurona
    teta = -0.5 # Umbral de la neurona
    
    """Función de la neurona."""
    n = w*d

    flag = n >= teta

    if flag:
        a = 1
    else:
        a = 0

    if a == t:
       return  a, "exito"
    else:
        return a, "error en la ejecución de la neurona" 

if __name__ == "__main__":
    main()

    d1, d2 = 0,1 # Variables de entrada
    t1, t2 = 1,0 # Variables de salida

    # Compuerta NOT:

    out, error = neuronNOT(d1,t1)
    print("Resultado: ", out, error)

    out, error = neuronNOT(d2,t2)
    print("Resultado: ", out, error)


    
    
    





 
