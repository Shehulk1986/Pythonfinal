#Definir variables

inicio = 0 # Número de inicio del rango
fin = 0 # Número del fin del rango
numeros_impares =[0,100]# Lista de números impares

#Solicitar al usuario que ingrese el número de rango


inicio = int(input("Ingrese el numero de inicio del rango:"))
fin = int(input("Ingrese el numero de fin del rango: "))

# Recorre el rango de números y encontrar los números impares
 
for numero in range(inicio, fin + 1):
     if numero % 2 !=0:
         numeros_impares.append(numero) # append agrega un elemento al final de la lista
         
# Imprimir los números impares
print("Los numeros impares dentro del rango son:")     
print(numeros_impares)  



