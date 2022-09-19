#Uma fábrica controla o tempo de trabalho sem acidentes pela quantidade de dias. Faça um
#algoritmo para converter este tempo em anos, meses e dias. Assuma que cada mês possui sempre 30 dias.

days = float(input("Digite a quantidade de dias sem acidentes nesta empresa: "))

month = days//30
year =  month//12

print(f"Esta empresa está a {days} dias, {month} meses e {year} anos sem acidentes no trabalho.")
