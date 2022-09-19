nome = str(input("Digite o seu nome:"))
turno = str(input("Digite o turno que você estuda:"))

if turno == "M":
    print(f"Bom dia {nome}!")

elif turno == "m":
    print(f"Bom dia {nome}!")

elif turno == "V":
    print(f"Boa tarde {nome}!")

elif turno == "v":
    print(f"Boa tarde {nome}!")

elif turno == "N":
    print(f"Boa noite {nome}!")

elif turno == "n":
    print(f"Boa noite {nome}!")

else:
    print("Valor inválido!")