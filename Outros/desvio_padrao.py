#Desvio Padrão
#Gustavo Paulo
conj = [6,2,3,1]
somatorio = 0

#Etapa 1 - calcular a média
media = sum(conj) / len(conj)

#Etapa 2 e 3 - calcular o quadrado da distância entre cada ponto e a média.
#Somar os valores da Etapa 2
for dado in conj:
    somatorio += (dado - media)**2

#Etapa 4 - dividir pelo número de pontos
N = somatorio/media

#Etapa 5 - calcular a raiz quadrada
raiz = (N**(0.5))

print("Resultado: %.2f" % raiz)