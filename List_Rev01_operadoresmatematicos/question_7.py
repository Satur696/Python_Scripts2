#Faça um algoritmo para ler o salário de um funcionário e aumentá-lo em 15%.
#Após o aumento, desconte 8% de impostos. Imprima o salário inicial, o salário com o aumento
#e o salário final.

salario = float(input("Digite o salário deste funcionário: "))
aumento = (salario*0.15)+salario
desconto = aumento-(aumento*0.08)

print(f"O funcionário ganhava anteriormente R${salario}\nO mesmo teve um aumento de 15% é passou a ganhar R${aumento}\nPorém ele teve um desconto em imposto de 8% e passou a ficar com R${desconto}\nLogo o total de salário que ele recebeu foi de R${desconto}")