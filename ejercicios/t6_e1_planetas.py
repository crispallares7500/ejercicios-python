def planetas():
    planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

    numero = int(input("Introduce un número del 1 al 8: "))
    if 1 <= numero <= 8:
        print("El planeta en la posición", numero, "es", planetas[numero - 1])
    else:
        print("Número inválido. Por favor, introduce un número del 1 al 8.")    
planetas()