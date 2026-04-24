def calcular_nota_media():
    cantidad = int(input("¿Cuántas notas quieres introducir? "))

    suma = 0
    for i in range(cantidad):
        nota = float(input(f"Introduce la nota {i + 1}: "))
        suma += nota

    media = suma/cantidad
    print("La nota media es:", media)

calcular_nota_media()
