precio_camiseta = 10
precio_sudadera = 20.5
precio_gorra = 5.5

cantidad_camisetas = int(input("¿Cuántas camisetas quieres?: "))
cantidad_sudaderas = int(input("¿Cuántas sudaderas quieres?: "))
cantidad_gorras = int(input("¿Cuántas gorras quieres?: "))

BI = (precio_camiseta * cantidad_camisetas) + (precio_sudadera * cantidad_sudaderas) + (precio_gorra * cantidad_gorras)
IVA = BI * 0.21
total_pagar = BI + IVA

print("Base Imponible: ", BI, "€")
print("IVA 21%: ", IVA, "€")
print("Total a pagar: ", total_pagar, "€")
