#Questão 4
#A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista
T = [-10, -8, 0, 1, 2, 5, -2, -4]
#Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.
media = sum(T)/len(T)
print(f'> A média de temperatura é: {media} °C')
T.sort()
print(f'> Mais alta: {T[7]} °C')
print(f'> Mais baixa: {T[0]} °C')