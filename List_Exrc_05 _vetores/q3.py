temp = []
meses = ["Janeiro", 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
cont = 0

for t in range(0, len(meses)):
    mes = float(input(f"Digite a temperuta do mês de " + meses[t] + ': '))
    temp.append(mes)

media_anual = sum(temp)/12

print()
print('--'*30)
print(f"Média da temperatura anual: {media_anual}")
print("Os meses com temperatura acima da média anual, tais são:")
for x in range(0, len(temp)):
    if temp[x] > media_anual:
        print(str(x+1) + ' - ' + meses[x])

print(f"\nDada a matriz:\n{temp}")