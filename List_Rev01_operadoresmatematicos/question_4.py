# O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. 
# Escreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. 
# Assuma que a balança já desconte o peso do prato.

refeicao = 12
prato = float(input("Digite o peso do prato: "))
valor_a_pagar = refeicao*prato
print(f"O cliente irá pagar {valor_a_pagar}")