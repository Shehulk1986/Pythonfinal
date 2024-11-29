#Valor pagar cliente

def val()

Valor = int(input("ingrese el Valor a pagar:"))

if Valor > 20000:
    Pago = Valor * 0.8
    print("Valor a pagar es de:" , Pago)
    
else:
    print("El Valor a pagar se mantiene igual:" , Valor)
    