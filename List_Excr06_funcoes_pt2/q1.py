def recive():
    argumento1 = float(input('Digite o 1º Argumento: '))
    argumento2 = float(input('Digite o 2º Argumento: '))
    argumento3 = float(input('Digite o 3º Argumento: '))
    return argumento1, argumento2, argumento3

def soma(argumento1, argumento2, argumento3):
    sum = (argumento1+argumento2+argumento3)
    return sum

def med(sum):
    media = (sum/3)
    return media

def show(sum, media):
    print(f'|| A soma entre os três argumentos é: {sum}')
    print(f'|| A média entre esses argumento é: {media}')

a1, a2, a3 = recive()
soma_arg = soma(a1, a2, a3)
med_ia = med(soma_arg)
show(soma_arg, med_ia)