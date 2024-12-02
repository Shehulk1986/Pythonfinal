
# Definir variables
nombre = ""
asignatura = ""
nota1 = 0
nota2 = 0
nota3 = 0
calificacion_final = 0

#Pedir al usuario su nombre, asignatura y notas de los exámenes
nombre = input("Ingrese su nombre: ")
asignatura = input("Ingrese la asignatura: ")
nota1 = float(input("Ingrese la nota del primer examen (0-5): "))
nota2 = float(input("Ingrese la nota del segundo examen (0-5): "))
nota3 = float(input("Ingrese la nota del último examen (0-5): "))

#Calcular la calificación final
calificacion_final = (nota1 * 0.3) + (nota2 * 0.3) + (nota3 * 0.4)

#Determinar si el aprendiz aprueba o no
if calificacion_final >= 4.0:
    print(f"Felicidades {nombre}, has aprobado la asignatura {asignatura} con una calificación final de {calificacion_final:.2f}.")
else:
    print(f"Lo siento {nombre}, no has aprobado la asignatura {asignatura}. Tu calificación final es {calificacion_final:.2f}.")
