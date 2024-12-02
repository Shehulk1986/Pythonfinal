#Valor pagar cliente

#Definir variables
precio = 0
precio_final = 0

#Pedir al usuario el precio
precio = float(input("Ingrese el precio del producto: $"))

#Calcular el precio final
if precio > 20000:
    descuento = precio * 0.20
    precio_final = precio - descuento
else:
    precio_final = precio

#Imprimir el precio final
print(f"El precio final a pagar es: ${precio_final:.2f}")
