#A granja Frangotech possui um controle automatizado de cada frango da sua produção. No pé
#direito do frango há um anel com um chip de identificação; no seu pé esquerdo são dois anéis
#para indicar o tipo de alimento que ele deve consumir. Sabendo que o anel com chip custa R$4,00
#e o anel de alimento custa R$3,50, faça um algoritmo para calcular o gasto total da granja
#para marcar todos os seus frangos.

frangos = int(input("Digite a quantidade de frangos nesta fábrica: "))

anel_chip = 4
anel_alimento = 3.50

pe_d = anel_chip
pe_e = 2*anel_alimento

gasto = (frangos*pe_d)+(frangos*pe_e)

print(f"Será um gasto de R${gasto} para marcar todos os {frangos} frangos desta fábrica.")