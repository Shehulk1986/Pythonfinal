#Solicitar al usuario que ingrese el numero

# Definir variable
n = 0

# Pedir al usuario que ingrese un número entero
n = int(input("ingrese un numero entero:"))

# Calcular y mostrar factorial
factorial = 1
    
for i in range(1,n + 1):
        factorial *= i

#Mostrar el resultado

print(f"El factorial de {n} es:{factorial}")    