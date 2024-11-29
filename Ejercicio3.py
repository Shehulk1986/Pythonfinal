#Definir variable

numeros_a_mostrar = 50 # Número máximo a mostrar
saltos_de_linea = 7 # Número de números por linea 

# Mostrar números con saltos de línea

for i in range(1, numeros_a_mostrar + 1):
    print(i, end='')
    if i % saltos_de_linea == 0:
        print()
        