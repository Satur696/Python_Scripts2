n = 0
soma = 0

while n < 500:
    if n%2 == 1:
        soma = n+soma
    n += 1
print(f"A soma dos número impáres de 1 a 500 é: {soma}")