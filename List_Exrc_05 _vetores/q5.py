intervalos = [0]*9
cont = 0
while True:
   salario = float(input(f'Informe o {cont + 1}° salário. [0 ou negativo = break]\nR$'))
   if salario <= 0:
      break
   if salario < 200:
      print(f'Salário não pode ser 
      menor que 200. Tente novamente')
      continue
   posicao = int(salario // 100 - 2)
   if posicao > 8:
      posicao = 8
   intervalos[posicao] += 1
   cont += 1
print(f'A quantidade de salários nas faixas citadas são: {intervalos}')