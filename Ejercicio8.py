# Definir variables

edad = 0
sexo = ""

#Pedir al usuario su edad y sexo
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo (H/M): ")

#Verificar si el usuario puede  jubilarse
if sexo.upper() == "H" and edad >= 63:
    print("Usted ya puede jubilarse.")
    
elif sexo.upper() == "M" and edad >= 54:
    print("Usted todavia no puede jubilarse.")