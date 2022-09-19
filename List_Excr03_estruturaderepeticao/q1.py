alt_ma = 0
alt_me = 0

for a in range(1,16):
    altura = float(input(f'Altura da {a}ª pessoa:'))
    if a == 1:
        maior = altura
        menor = altura
    else:
        if altura > maior:
            maior = altura
        if altura < menor:
            menor = altura

print(f"A maior altura foi de {maior}m")
print(f"A menor altura foi de {menor}m")