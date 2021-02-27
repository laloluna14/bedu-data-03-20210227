lista = [
    10,
    30,
    45,
    90,
    89,
    1,
    9
]

# Ordernar
lista.sort()

for elemento in lista:
    print(elemento)

# Longitud lista
print(f'La longitud de la lista es de {len(lista)} elementos')

# Remover un elemento
print(lista)
lista.pop()
print(lista)

# Agregar elemento
lista.append(56)
lista.append(20)
lista.append(2)

print(lista)
