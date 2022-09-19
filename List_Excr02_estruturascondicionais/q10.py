salario = float(input("Digite o salário do colaborador: R$"))

s_20 = 0.2
s_15 = 0.15
s_10 = 0.1
s_5 = 0.05

print(f"Antes do reajuste o colaorador recebia: R${salario}")

if salario <= 280:
    ajuste = salario*s_20
    print("Houve um aumento de 20%")

elif salario > 280 and salario < 700:
    ajuste = salario*s_15
    print("Houve um aumento de 15%")

elif salario >= 700 and salario < 1500:
    ajuste = salario*s_10
    print("Houve um aumento de 10%")

elif salario >= 1500:
    ajuste = salario*s_5
    print("Houve um aumento de 5%")

else:
    print("Erro!")

print(f"O valor de aumento foi de R${ajuste}")
print(f"O novo salário, após este aumento é de R${salario+ajuste}")