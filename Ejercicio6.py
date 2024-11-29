# Defina varibles
tasa_cambio = 3.934 # tasa de cambio de dólares a pesos
dolares = 0 # Cantidad de dólares a convertir
pesos = 0 # Cantidad de pesos equivalente 
continuar = 's' # Variable para controlar la ejecución del programa

# Estructura while para realizar converciones 
while continuar.lower() == 's':
    # Pedir al usuario la cantidad de dólares de dólares a convertir
    dolares = float(input("Ingresa la cantidad de dólaress a convertir: "))
    
    # Calcular la cantidad de pesos equivalente
    pesos = dolares*tasa_cambio
    
    # Mostrar el resultado de la converción
    print(f"{dolares} dólars equivalen a {pesos:2f}) pesos")
    
    # Preguntar al usuario si desea seguir realizando conversiones
    continuar = input("¿Desea seguir realizando conversiones? (s/n):")
    
    # Validar la entrada del usuario
    while continuar.lower() not in ['s','n']:
        continuar = input("Entrada inválida. ¿Desea seguir realizando conversiones? (s/n)")
    
    # Mostrar mensaje de despedida    
    print("Gracias por utilizar el conversor de dólares a pesos")
    