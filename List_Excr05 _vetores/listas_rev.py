lista = []

lista.append("ana clara")
lista.append("michel arthur")
lista.append("keury motoca")
lista.append("daniela")
lista.append("mariaDB")

for y in lista:
    print(y)

lista.remove("daniela")

lista.insert(0, "elivan")

for y in lista:
    print(y)

lista2 = ["bola", "futebol"]

soma_lista = lista + lista2
print(soma_lista)

print(sorted(lista))