perg = ["A. Telefonou para a vítima?", "B. Esteve no local do crime?", "C. Mora perto da vítima?", "D. Devia para a vítima?", "E. Já trabalhou com a vítima?"]
resp = []
cont = 0

print('\nNa resposta do questionário:\nUtilize 1 - para sim e 0 - para não\n')
for h in range(len(perg)):
    print(perg[h])
    resp.append(input(" "))
    cont += int(resp[h])

print('--'*30)
print()
print("Julgamento!\n")
status = ["Inocente","Suspeita","Cúmplice","Cúmplice","Assassino"]
if cont < 2:
    print("Você é: " + status[0]) 
else:
    print("Você é: " + status[cont-1])