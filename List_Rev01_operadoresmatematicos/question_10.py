#A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias
#de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de
#queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um
#algoritmo em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as
#quantidades (em quilos) de queijo, presunto e carne necessários para compra.

sanduiche = int(input("Digite a quantidade de sanduíches que deseja fazer: "))

queijo = 50
presunto = 50
hamburguer = 100

qtd_queijo = sanduiche*queijo
qtd_presunto = sanduiche*presunto
qtd_hamburguer = sanduiche*hamburguer

qtd_qph = qtd_queijo+qtd_presunto+qtd_hamburguer

print(f"Será necessário {qtd_qph}g/{qtd_qph//1000}kg de queijo, presunto e carne para comprar")