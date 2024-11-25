#Solicitar al usuario que ingrese el numero

n = int(input("ingrese un numero entero:"))

#Validar que el numero sea positivo
if n < 0:
    print("error: el numero debe ser positivo.")
    
else:
    #Calcular el factorial
    factorial = 1
    
    for i in range(1,n+1):
        factorial *= i
    
    print("factorial de",n,":",factorial)    