#Definir la variable
def imprimir_impares(init, end):
    for numero in range(init, end +1):
    if numero % 2 !=0:
        print(numero)

#Solicitar al usuario que ingrese el número de rango

init = int(input("Ingrese el número de inicio del rango:"))
end = int(input("Ingrese el número de fin del rango "))

if init > end:
    print("el número inicial debe ser mayor al numero final")
    
else:
    imprimir_impares(init, end)
    



