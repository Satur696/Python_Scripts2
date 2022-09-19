#A padaria hotpão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia. 
#cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia, o dono quer saber quanto arrecadou 
#com a venda dos pães e broas (juntos), e quanto deve guardar numa conta de poupança (10% do total arrecadado). 
#Você foi contradado para fazer os cálculos para o dono. Com base nestes fatos, 
#faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular os dados solicitados.

broas = 1.50
paes = 0.12
qtd_broas = int(input("Digite a quantidade de broas vendidos:"))
qtd_paes = int(input("Digite a quantidade de pães vendidos:"))
faturamento = (broas*qtd_broas) + (paes*qtd_paes)
print(f"O faturamento do dono foi de R${faturamento}")
poupanca = faturamento*0.1
print(f"O dono deverá guardar R${poupanca} na sua conta poupança")