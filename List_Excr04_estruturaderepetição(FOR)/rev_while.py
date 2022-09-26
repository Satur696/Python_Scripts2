filhos = 0
cont_pessoas = 0
cont_pessoas100 = 100
salario = 0
media_salario = 0
media_filhos = 0
porcentagem_salario = 0
maior_salario = 0
contador = 0

while (contador >=0):
    salario = float(input("Digite o salário desta pessoa (para encerrar o bloco de código digite um número negativo): R$"))
    if (salario >= 0):
        cont_pessoas += 1
        media_salario += salario
        if (salario <= 100):
            cont_pessoas100 += 1
        if(salario>maior_salario):
            maior_salario = salario
    filhos = int(input("Digite o número de filhos desta pessoa: "))
    media_filhos += filhos

    if (salario < 0):
        break

    porcentagem_salario = (cont_pessoas100*100)//cont_pessoas
    
contador += 1

print(f"A media do salário da população é: {media_salario/cont_pessoas}")
print(f"A media do número de filhos da população é: {media_filhos/cont_pessoas}")
print(f"O maior salário é: {maior_salario}")
print(f"A porcentagem de pessoas com salário de até R$100,00 é: {porcentagem_salario}%")