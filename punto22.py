# Solicitar 10 numeros , almacenarlos en una lista y determinar el mayor y el menor 

ListStorage = []

for i in range(10):
    number = int(input("Escribe un Número: "))
    ListStorage.append(number)

    if i == 0:
        mayor = number
        menor = number
    else:
        if number > mayor:
            mayor = number
        if number < menor:
            menor = number

print(f"El Número Menor es: {menor}")
print(f"El Número Mayor es: {mayor}")
print(f"La Listica completa: {ListStorage}")