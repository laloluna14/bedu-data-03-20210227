suma_dos_elementos = lambda x, y: x + y
print(suma_dos_elementos(10, 2))


listado_precios = [2000, 4000, 6000, 8000]
listado_precios_con_iva = list(map(lambda n: n*1.16, listado_precios))
print(listado_precios_con_iva)
