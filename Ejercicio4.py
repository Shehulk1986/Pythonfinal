# Definir variables
capital_inicial = 0 # Cantidad de dinero a invertir
interes_anual = 0 # Interés anual
años_inversion = 0 # Años de inversión
capital_final = 0 # Capital obtenido en la inversión

#Pedir al usuario la cantidad de dinero a invertir 
capital_inicial = float(input("Ingrese la cantidad de dinero a invertir:"))

#Pedir al usuario el interés anual
interes_anual = float(input("Ingrese el interés anual en porcentaje: ")) 

#Pedir al usuario los años de inversión
años_inversion = int(input("Ingrese los años de inversión: "))

#Calcular el capital obtenido en la inversión
capital_final = capital_inicial * (1 + (interes_anual / 100)) ** años_inversion

#Mostrar por pantalla el capital obtenido en la inversión
print(f"El capital obtenido en la inversión e: $ {capital_final:.2f}")