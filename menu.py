#principal.py

import time
from punto7 import compra
from punto24 import  procesar_duplicados
from punto15 import fibonacci
def mostrar_menu():
    while True: 
        print("---------Menu----------")
        print("1. Procesar duplicados(Punto 24)")
        print("2. Descuentos(Punto 7)")
        print("3. Mayor y menor(Punto 22)")
        print("4. Fibonacci(Punto 15)")
        print("5. Salir")

        try:
            opcion=int(input("Ingrese una opción: "))
            if opcion==1:
                procesar_duplicados()
                time.sleep(1)
            elif opcion==2:
                compra()
                time.sleep(1)
            elif opcion==3:
                print("Funcionalidad de mayor y menor aún no implementada.")
            elif opcion==4:
                fibonacci()
                time.sleep(1)
            elif opcion==5:
                print ("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, ingrese un número del 1 al 5.")
                time.sleep(1)

        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero...")
            time.sleep(1)

        
if __name__=="__main__":
    mostrar_menu()