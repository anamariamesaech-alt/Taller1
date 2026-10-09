compra=float(input("ingresa el valor de la compra: "))

if compra >= 100000:
    descuento = compra * 0.05
elif compra >= 300000:
    descuento = compra * 0.10
elif compra >= 500000:
    descuento =compra * 0.15
else:
    descuento = 0
    
total= compra - descuento

print(f"valor de la compra {compra}")
print(f"valor del descuento {descuento}")
print(f"valor final {total}")
