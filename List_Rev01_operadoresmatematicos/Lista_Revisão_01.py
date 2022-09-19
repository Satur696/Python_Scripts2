#Nota: Este arquivo python reune todos os código separados na pasta em um único código só.
#Eu recomendo que para este código funcione de maneira adequada inicie ele.

print("Informática - 2º Ano")
print("Aluno: Gustavo Paulo dos Santos")

print()
print("Questão 01. A imobiliária Imóbilis vende apenas terrenos retangulares.\nFaça um algoritmo para ler as dimensões de um terreno e depois exibir a área do terreno.")
print()

dimensao_a = float(input("Digite o valor da altura: "))
dimensao_b = float(input("Digite o valor da base: "))
area = dimensao_a*dimensao_b

print(f"A área deste terreno é: {area} M²")

print("Questão 02. Faça um algoritmo para calcular quantas ferraduras são necessárias para equipar todos os cavalos comprados para um haras")
print()

qtd_cavalos = float(input("Digite a quantidade de cavalos no haras: "))
ferraduras = qtd_cavalos*4
print(f"Serão necessárias {int(ferraduras)} ferraduras para equipar os {int(qtd_cavalos)} cavalos.")

print()
print("Questão 03. A padaria hotpão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia.\nCada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. Ao final do dia,\no dono quer saber quanto arrecadou com a venda dos pães e broas (juntos),\ne quanto deve guardar numa conta de poupança (10% do total arrecadado).\nVocê foi contradado para fazer os cálculos para o dono.\nCom base nestes fatos, faça um algoritmo para ler as quantidades de pães e de broas,\ne depois calcular os dados solicitados.")
print()

broas = 1.50
paes = 0.12
qtd_broas = int(input("Digite a quantidade de broas vendidos:"))
qtd_paes = int(input("Digite a quantidade de pães vendidos:"))
faturamento = (broas*qtd_broas) + (paes*qtd_paes)
print(f"O faturamento do dono foi de R${faturamento}")
poupanca = faturamento*0.1
print(f"O dono deverá guardar R${poupanca} na sua conta poupança")

print()
print("Questão 04. O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição.\nEscreva um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar.\nAssuma que a balança já desconte o peso do prato.")
print()

refeicao = 12
prato = float(input("Digite o peso do prato: "))
valor_a_pagar = refeicao*prato
print(f"O cliente irá pagar {valor_a_pagar}")

print()
print("Questão 05. Entrar com o dia e o mês de uma data e informar quantos dias se passaram desde o início do ano.\nEsqueça a questão dos anos bissextos e considere sempre que um mês possui 30 dias.")
print()
dia = int(input("Digite um dia: "))
mes = int(input("Digite um mês (em número): "))

calc_dias = (30*(mes-1)+dia)

print(f"Já se passaram: {calc_dias} dias, desde a data informada {dia}/{mes}")

print()
print("Questão 06. Uma fábrica controla o tempo de trabalho sem acidentes pela quantidade de dias.\nFaça um algoritmo para converter este tempo em anos, meses e dias. Assuma que cada mês possui sempre 30 dias.")
print()

days = float(input("Digite a quantidade de dias sem acidentes nesta empresa: "))

month = days//30
year =  month//12

print(f"Esta empresa está a {days} dias, {month} meses e {year} anos sem acidentes no trabalho.")

print()
print("Questão 07. Faça um algoritmo para ler o salário de um funcionário e aumentá-lo em 15%.\nApós o aumento, desconte 8% de impostos.\nImprima o salário inicial, o salário com o aumento e o salárioo final.")
print()

salario = float(input("Digite o salário deste funcionário: "))
aumento = (salario*0.15)+salario
desconto = aumento-(aumento*0.08)

print(f"O funcionário ganhava anteriormente R${salario}\nO mesmo teve um aumento de 15% é passou a ganhar R${aumento}\nPorém ele teve um desconto em imposto de 8% e passou a ficar com R${desconto}\nLogo o total de salário que ele recebeu foi de R${desconto}")

print()
print("Questão 08. Calcule a área de uma pizza que possui um raio R (pi=3.14)")
print()

pizza = float(input("Digite o raio da pizza: "))
pi = 3.14
area = pi*pizza**2

print(f"A área dessa pizza é igual a {area} cm")

print()
print("Questão 09. Três amigos, Carlos, André e Felipe. decidiram rachar igualmente a conta de um bar.\nFaça um algoritmo para ler o valor total da conta e imprimir quanto cada um deve pagar,\nmas faça com que Carlos e André não paguem centavos. Ex: uma conta de R$101,53 resulta\nem R$33,00 para Carlos, R$33,00 para André e 35,53 Para Felipe.")
print()

vlr_conta = float(input("Digite o valor da conta: R$"))

racha = vlr_conta//3

carlos = racha
andre = racha
felipe = (vlr_conta%3)+racha

print(f"A conta de R${vlr_conta} resulta em R${carlos} para Carlos, R${andre} para André e R${felipe} para Felipe.")

print()
print("Questão 10. A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui duas fatias\nde queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo que cada fatia de\nqueijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer pesa 100 gramas, faça um\nalgoritmo em que o dono forneça a quantidade de sanduíches a fazer, e a máquina informe as\nquantidades (em quilos) de queijo, presunto e carne necessários para compra.")
print()

sanduiche = int(input("Digite a quantidade de sanduíches que deseja fazer: "))

queijo = 50
presunto = 50
hamburguer = 100

qtd_queijo = sanduiche*queijo
qtd_presunto = sanduiche*presunto
qtd_hamburguer = sanduiche*hamburguer

qtd_qph = qtd_queijo+qtd_presunto+qtd_hamburguer

print(f"Será necessário {qtd_qph}g/{qtd_qph//1000}kg de queijo, presunto e carne para comprar")

print()
print("Questão 11. A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 por hora extra.\nFaça um algoritmo para calcular e imprimir o salário bruto e o salário líquido de um\ndeterminado funcionário. Considere que o salário líquido é igual ao salário bruto descontando-se\n10% de impostos.")
print()

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

print()
print("Questão 12. A granja Frangotech possui um controle automatizado de cada frango da sua produção. No pé\ndireito do frango há um anel com um chip de identificação; no seu pé esquerdo são dois anéis\npara indicar o tipo de alimento que ele deve consumir. Sabendo que o anel com chip custa R$4,00\ne o anel de alimento custa R$3,50, faça um algoritmo para calcular o gasto total da granja\npara marcar todos os seus frangos.")
print()

frangos = int(input("Digite a quantidade de frangos nesta fábrica: "))

anel_chip = 4
anel_alimento = 3.50

pe_d = anel_chip
pe_e = 2*anel_alimento

gasto = (frangos*pe_d)+(frangos*pe_e)

print(f"Será um gasto de R${gasto} para marcar todos os {frangos} frangos desta fábrica.")

print()
print("Questão 13. Uma confecção produz X blusas de lã e para isto gasta uma certa quantidade de novelos. Faça um algoritmo para calcular quantos novelos de lã ela gasta por blusa")
print()

blusas = int(input("Digite a quantidade de blusas de lã produzidas pela confecção: "))
novelo = int(input("Digite a quantidade de novelos de lã: "))

novelos_gastos = novelo//blusas

print(f"É gastado cerca de {novelos_gastos} novelos de lã por cada blusa produzida.")

print()
print("Questão 14. A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: lata de 350 ml,\ngarrafa de 600ml e garrafa de 2 litros. Se um comerciante compra uma determinada quantidade\nde cada formato, faça um algoritmo para calcular quantos litros de refrigerante ele comprou.")
print()

lata = int(input("Digite a quantidade de latas de refrigerante que este comerciante comprou: "))
garrafa_600 = int(input("Digite a quantidade de garrafas de refrigerante (600ml) que este comerciante comprou: "))
garrafa_2 = int(input("Digite a quantidade de garrafas de refrigerante (2l) que este comerciante comprou: ")) 

ml_lata = 350*lata
ml_garrafa600 = 600*garrafa_600
l_garrafa2 = 2000*garrafa_2

qtd_litros = (ml_lata+ml_garrafa600+l_garrafa2)//1000

print(f"Este comerciante comprou {qtd_litros}l/{qtd_litros*1000}ml de refrigerante.")
