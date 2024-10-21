#a)
lista = [x for x in range(5)]
print(lista)

#b)
lista = list(range(5))
print(lista)

#c)
lista = []
i = 0
while i<5:
    lista.append(i)
    i += 1
    print(lista)
