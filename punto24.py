#Procesador
def  procesar_duplicados():
    entrada= input("Ingrese una lista de números separados por espacios: ")
    lista=entrada.split()

    repetidos=[]
    sin_repetido=[]

    for elemento in lista:
        if elemento not in sin_repetido:
            sin_repetido.append(elemento)
        elif elemento  not in repetidos:
            repetidos.append(elemento)

    print("---------Resultados----------")
    print("Elementos repetidos:", repetidos)
    print("Lista sin elementos repetidos:", sin_repetido)