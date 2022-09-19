quant = 0
s= 0

while True:
    n_r = float(input("Digite um número: "))
    if n_r == 0:
        break
    s += n_r
    quant += 1

print(f"A quantidade de número digitados foi: {quant}")
print(f"Média: {s/quant}")