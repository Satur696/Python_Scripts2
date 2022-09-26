vetor = []
mult = 1
soma = 0

for n in range (5):
    num = int(input("Digite um número: "))
    vetor.append(num)
for y in vetor:
    mult *= y
for x in vetor:
    soma += x

print(f"A soma dos números são {soma}, a multiplicação {mult} e a lista é {vetor}.")