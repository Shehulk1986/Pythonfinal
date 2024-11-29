# Definir variables
notas = 0 # Número de notas
suma_notas = 0 # Suma de las notas
promedio = 0 # Promedio de las notas
nota_actual = 0 # Nota actual

# Pedir al profesor el número de notas
notas = int(input("Ingrese el número de notas:"))

#Utilizar estructura while para pedir las notas y calcular el promedio

i = 1
while i <= notas:
    nota_actual = float(input(f"Ingrese la nota {i}:"))
    suma_notas += nota_actual
    i += 1

#Calcular el promedio
promedio = suma_notas / notas

#Determinar si el estudiante aprueba o no if promedio >= 4.5:
if promedio >= 4.5:
      print(f"El estudiante aprueba con un promedio de {promedio:.2f}")

else:
    print(f"El estudiante no aprueba con un promedio de {promedio:.2f}")
    