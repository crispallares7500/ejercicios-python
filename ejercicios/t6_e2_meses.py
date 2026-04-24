def meses ():
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    numero = int(input("Introduce un número del 1 al 12: "))

    if 1<= numero <= 12:
        mes = meses[numero - 1]
        print("El mes es", mes)

        if mes == "Junio":
            print("EL MEJOR MES")

    else:   
        print("Número inválido. Por favor, introduce un número del 1 al 12.")

meses()
        
        
