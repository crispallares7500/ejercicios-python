cantidad_euros = float(input("Introduzca la cantidad de euros a convertir: "))
dolares = cantidad_euros * 1.1
libras = cantidad_euros * 0.87
print("La cantidad en dólares es: ", dolares, "$")
print("La cantidad en libras es: ", libras, "£")


# otra manera con funciones
def convertir_euros_a_dolares(cantidad_euros):
    resultado = cantidad_euros * 1.1
    return resultado

def convertir_euros_a_libras(cantidad_euros):   
    resultado = cantidad_euros * 0.87
    return resultado    

def conversor():
    cantidad_euros = float(input("Introduzca la cantidad de euros a convertir: "))
    
    print("Convertir en Dolares")
    cantidad_en_dolares = convertir_euros_a_dolares(cantidad_euros)
    print("La cantidad en dólares es: ", cantidad_en_dolares, "$")
    
    print("Convertir en Libras")
    cantidad_en_libras = convertir_euros_a_libras(cantidad_euros)
    print("La cantidad en libras es: ", cantidad_en_libras, "£")

conversor()
