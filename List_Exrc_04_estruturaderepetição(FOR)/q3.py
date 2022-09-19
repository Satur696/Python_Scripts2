numero = int(input("Digite um número: "))
fatorial = 1

for a in range(1, numero):
    fatorial *= numero
    numero -= 1
print(f"O fatorial do número é: {fatorial}")