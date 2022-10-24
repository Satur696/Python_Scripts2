#Questão 3
#Faça um programa que percorra duas listas e que gere uma terceira sem elementos repetidos.

x = []
y = []
max = 0
while True:
  x.append(input('> Digite os elementos da lista 1: '))
  y.append(input('> Digite os elementos da lista 2: '))
  max += 1
  if x[max-1] == '0' or y[max-1] == '0':
    break

for tt1 in x:
  for tt2 in y:
    if (tt1==tt2):
        print(list(set(x+y)))