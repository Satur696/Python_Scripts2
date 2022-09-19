number = float(input("Digite um número:"))

print(f"O número digitado foi {number}")

if number > 0:
    print(f"O número {number} é positivo (+)")

elif number < 0:
    print(f"O número {number} é negativo (-)")

elif number == 0:
    print(f"{number} é neutro")

else:
    print("Erro!")