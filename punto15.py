# Serie de fibonacci

numero = int(input("¿Cuántos números de la serie de fibonnaci deseas ver?: "))
a = 0
b = 1

for i in range(numero):
    print(a)
    
    siguiente = a + b
    a = b
    b = siguiente 