#Uma confecção produz X blusas de lã e para isto gasta uma certa quantidade de novelos.
#Faça um algoritmo para calcular quantos novelos de lã ela gasta por blusa

blusas = int(input("Digite a quantidade de blusas de lã produzidas pela confecção: "))
novelo = int(input("Digite a quantidade de novelos de lã: "))

novelos_gastos = novelo//blusas

print(f"É gastado cerca de {novelos_gastos} novelos de lã por cada blusa produzida.")
