producto = input("Ingrese el nombre del producto: ")
precio_unitario = float(input("Ingrese el precio del producto: "))
cantidad_comprar = int(input("Ingrese la cantidad a comprar: ")) 
descuento = float(input("Ingrese el descuento en porcentaje: "))   
IVA = float(input("Ingrese el IVA en porcentaje: "))
BI = precio_unitario * cantidad_comprar 
precio_total = BI - (BI * descuento / 100) + (BI * IVA / 100)
print("El precio total es: ",  precio_total, "€")

