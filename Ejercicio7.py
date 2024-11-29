#Definir variables
nombre_aprendiz = "" # Nombre del aprendiz
materia = "" # Asignatura
calificacion_final = 0 # Calificación final

# ingresar datos del aprendiz
nombre_aprendiz = input("Ingrese el nombre del aprendiz: ")
materia = input("ingresa el nombre del materia: ")

# Ingresar calificación final y validar que esté entre 1 y 10

while True:
  try:
        calificacion_final = float(input("Ingrese la calificación final(1-10): "))
        if 1 <= calificacion_final <=10:
          break
        else:
            print("La calificación debe estar entre 1 y 10.")

  except ValueError:
    print("La calificación debe ser un número.")   
    
# Mostrar información en pantalla         
print("'/nInformación del aprendiz:")
print(f"Nombre: {nombre_aprendiz}")
print(f"materia: {materia}")
print(f"Calificación final: {calificacion_final:.2f}")

# Determinar si el aprendiz aprobó o no 
if calificacion_final >=6:
    print("Resultado: Aprobado")
else:
    print("Resultado: No aprobado")
    