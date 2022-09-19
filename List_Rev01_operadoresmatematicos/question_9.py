#Três amigos, Carlos, André e Felipe. decidiram rachar igualmente a conta de um bar.
#Faça um algoritmo para ler o valor total da conta e imprimir quanto cada um deve pagar,
#mas faça com que Carlos e André não paguem centavos. Ex: uma conta de R$101,53 resulta
#em R$33,00 para Carlos, R$33,00 para André e 35,53 Para Felipe.

vlr_conta = float(input("Digite o valor da conta: R$"))

racha = vlr_conta//3

carlos = racha
andre = racha
felipe = (vlr_conta%3)+racha

print(f"A conta de R${vlr_conta} resulta em R${carlos} para Carlos, R${andre} para André e R${felipe} para Felipe.")

