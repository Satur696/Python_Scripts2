#A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 por hora extra.
#Faça um algoritmo para calcular e imprimir o salário bruto e o salário líquido de um deter
#minado funcionário. Considere que o salário líquido é igual ao salário bruto descontando-se
#10% de impostos.

funcionario = float(input("Digite quantas horas este funcionário trabalhou (apenas números): "))
hora_extra = float(input("Digite quantas horas extra este funcionário trabalhou (apenas números): "))

salario = 10*funcionario
salario_hrsext = 15*hora_extra

salario_bruto = salario+salario_hrsext

desconto = salario_bruto*0.1
salario_liquido = salario_bruto-desconto

print(f"""
O funcionário recebeu R${salario}, e recebeu R${salario_hrsext} de hora extra.
Logo, o salário bruto deste funcionário foi de R${salario_bruto}.
Porém foi descontado dele 10% em impostos. Portanto este funcionário recebeu R${salario_liquido}.
""")