#Solicitar al usuario que ingrese el numero

def calcular_factorial(n):
    if n < 0:
        return "Error: El factorial no está definido para números negativos."
    
    elif n == 0:
        return 1
    
    else:
        factorial = 1
    
    for i in range(1,n + 1):
        factorial *= i

# Pedir al usuario que ingrese un número entero


n = int(input("ingrese un numero entero:"))


# Calcular y mostrar factorial
factorial = calcular_factorial(n)


print(f"El factorial de {n} es:{factorial}")    