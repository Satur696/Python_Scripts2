#Atenção!!!!!!
#Este código junta todos os outros códigos "separados" em um único na linha de comando.
#Se algum código aqui der algum erro, tente consultá-lo individualmente na pasta.
#Obrigado!

import time

time.sleep(3.0)
print("Questão 1 (q1).")
print()

numb = float(input("Digite o primeiro número:"))
numb2 = float(input("Digite o segundo número:"))

print(f"Seus números digitados foram: {numb} e {numb2}")

if numb > numb2:
    print(f"O número {numb} é maior que o {numb2}")

elif numb2 > numb:
    print(f"O número {numb2} é maior que o {numb}")

time.sleep(3.0)
print()
print("Questão 2 (q2).")
print()

number = float(input("Digite um número:"))

print(f"O número digitado foi {number}")

if number > 0:
    print(f"O número {number} é positivo (+)")

elif number < 0:
    print(f"O número {number} é negativo (-)")

elif number == 0:
    print(f"{number} é neutro")

else:
    print("Erro!")

time.sleep(3.0)
print()
print("Questão 3 (q3).")
print()

sexo = str(input("Digite seu sexo:"))

if sexo == "F":
    print("Seu sexo é feminino")

elif sexo == "M":
    print("Seu sexo é masculino")

elif sexo == "m":
    print("Seu sexo é masculino")

elif sexo == "f":
    print("Seu sexo é feminino")

else:
    print("Sexo inválido")

time.sleep(3.0)
print()
print("Questão 4 (q4).")
print()

nota = float(input("Digite a primeira nota do aluno:"))
nota2 = float(input("Digite a segunda nota do aluno:"))

media = (nota+nota2)/2

if media == 7:
    print(f"A media do aluno foi {media}, logo foi Aprovado!")

if media == 8:
    print(f"A media do aluno foi {media}, logo foi Aprovado!")

if media == 9:
    print(f"A media do aluno foi {media}, logo foi Aprovado!")
    
elif media < 7:
    print(f"A media do aluno foi {media}, logo foi Reprovado!")

elif media > 9:
    print(f"A media do aluno foi {media}, logo foi Aprovado com Distinção!")

time.sleep(3.0)
print()
print("Questão 5 (q5).")
print()

numero_1 = float(input("Digite o primeiro número:"))
numero_2 = float(input("Digite o segundo número:"))
numero_3 = float(input("Digite o terceiro número:"))

if numero_1 > numero_2:
    if numero_1 > numero_3:
        print(f"O maior número, é {numero_1}")
    else:
        print(f"O maior número é {numero_3}")

elif numero_2 > numero_1:
    if numero_2 > numero_3:
        print(f"O maior número, é {numero_2}")
    else:
        print(f"O maior número é {numero_3}")

if numero_1 < numero_2:
    if numero_1 < numero_3:
        print(f"O menor número, é {numero_1}")
    else:
        print(f"O menor número é {numero_3}")

elif numero_2 < numero_1:
    if numero_2 < numero_3:
        print(f"O menor número, é {numero_2}")
    else:
        print(f"O menor número é {numero_3}")

else:
    "Todos os números são iguais!"

time.sleep(3.0)
print()
print("Questão 6 (q6).")
print()

precoProduto1 = float(input("Digite o preço do primeiro produto: R$"))
precoProduto2 = float(input("Digite o preço do segundo produto: R$"))
precoProduto3 = float(input("Digite o preço do terceiro produto: R$"))

if precoProduto1 < precoProduto2:
    if precoProduto1 < precoProduto3:
        print(f"O produto 1 custa R${precoProduto1}, portanto ele é o mais barato.")
    else:
        print(f"O produto 3 custa R${precoProduto3}, portanto ele é o mais barato.")

elif precoProduto2 < precoProduto1:
    if precoProduto2 < precoProduto3:
        print(f"O produto 2 custa R${precoProduto2}, portanto ele é o mais barato.")
    else:
        print(f"O produto 3 custa R${precoProduto3}, portanto ele é o mais barato.")

else:
    print("Todos os produtos tem o mesmo valor!")

time.sleep(3.0)
print()
print("Questão 7 (q7).")
print()

num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
num3 = float(input("Digite o terceiro número:"))

if num1 >= num2 and num2 >= num3:
    print(f"{num1}, {num2} e {num3}")

elif num2 >= num1 and num1 >= num3:
    print(f"{num2}, {num1} e {num3}")

elif num1 >= num3 and num1 >= num2:
    print(f"{num1}, {num3}, {num2}")
    
else:
    print(f"{num3}, {num2}, {num1}")

time.sleep(3.0)
print()
print("Questão 8 (q8).")
print()

nome = str(input("Digite o seu nome:"))
turno = str(input("Digite o turno que você estuda:"))

if turno == "M":
    print(f"Bom dia {nome}!")

elif turno == "m":
    print(f"Bom dia {nome}!")

elif turno == "V":
    print(f"Boa tarde {nome}!")

elif turno == "v":
    print(f"Boa tarde {nome}!")

elif turno == "N":
    print(f"Boa noite {nome}!")

elif turno == "n":
    print(f"Boa noite {nome}!")

else:
    print("Valor inválido!")

time.sleep(3.0)
print()
print("Questão 9 (q9).")
print()

numero = int(input("Digite o número para verificar se ele é impar ou par: "))

p_i = numero%2

if p_i == 1:
    print("Este número é impar")

elif p_i == 0:
    print("Este número é par")

else:
    print("Erro!")

time.sleep(3.0)
print()
print("Questão 10 (q10).")
print()

salario = float(input("Digite o salário do colaborador: R$"))

s_20 = 0.2
s_15 = 0.15
s_10 = 0.1
s_5 = 0.05

print(f"Antes do reajuste o colaorador recebia: R${salario}")

if salario <= 280:
    ajuste = salario*s_20
    print("Houve um aumento de 20%")

elif salario > 280 and salario < 700:
    ajuste = salario*s_15
    print("Houve um aumento de 15%")

elif salario >= 700 and salario < 1500:
    ajuste = salario*s_10
    print("Houve um aumento de 10%")

elif salario >= 1500:
    ajuste = salario*s_5
    print("Houve um aumento de 5%")

else:
    print("Erro!")

print(f"O valor de aumento foi de R${ajuste}")
print(f"O novo salário, após este aumento é de R${salario+ajuste}")