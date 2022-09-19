#A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: lata de 350 ml,
#garrafa de 600ml e garrafa de 2 litros. Se um comerciante compra uma determinada quantidade
#de cada formato, faça um algoritmo para calcular quantos litros de refrigerante ele comprou.

lata = int(input("Digite a quantidade de latas de refrigerante que este comerciante comprou: "))
garrafa_600 = int(input("Digite a quantidade de garrafas de refrigerante (600ml) que este comerciante comprou: "))
garrafa_2 = int(input("Digite a quantidade de garrafas de refrigerante (2l) que este comerciante comprou: ")) 

ml_lata = 350*lata
ml_garrafa600 = 600*garrafa_600
l_garrafa2 = 2000*garrafa_2

qtd_litros = (ml_lata+ml_garrafa600+l_garrafa2)//1000

print(f"Este comerciante comprou {qtd_litros}l/{qtd_litros*1000}ml de refrigerante.")