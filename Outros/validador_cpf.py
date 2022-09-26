print('== Validador de CPF ==\n')
CPF = input('|| Digite o CPF (sem dígitos e traços): ')

if len(CPF) > 11 or len(CPF) < 11:
    print('|| CPF Inválido.')

else:
#Verificar o 10º digito.
    sum = 0
    v = 10
    for i in range(0, len(CPF)-2):
        sum = sum + (int(CPF[i])*v)
        i+=1
        v-=1
    digito_1 = 11-(sum%11)
    if digito_1 >= 10:
        digito_1 = 0

#Verificar o 11º digito.
    sum = 0
    v = 10
    for x in range(1, len(CPF)-1):
        sum = sum + (int(CPF[x])*v)
        x+=1
        v-=1
    digito_2 = 11-(sum%11)
    if digito_2 >= 10:
        digito_2 = 0

if int(CPF[9]) != digito_1 or int(CPF[10]) != digito_2:
    print('|| CPF Inválido.')
else:
    print('|| CPF Válido.')