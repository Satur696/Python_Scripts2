

try:
    numero = int(input("Digite o número para verificar se ele é impar ou par: "))
except ValueError:
    print("Você deve digitar um número inteiro")
    exit("Saindo...")

p_i = numero%2

if p_i == 1:
    print("Este número é impar")

elif p_i == 0:
    print("Este número é par")

else:
    print("Erro!")