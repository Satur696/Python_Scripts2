#Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início
#do ano. Esqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias.

dia = int(input("Digite um dia: "))
mes = int(input("Digite um mês (em número): "))

calc_dias = (30*(mes-1)+dia)

print(f"Já se passaram: {calc_dias} dias, desde a data informada {dia}/{mes}")