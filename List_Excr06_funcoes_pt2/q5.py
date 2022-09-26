import random

def giradas():
    return random.randint(1,6)

def dado(x):
    cont1=cont2=cont3=cont4=cont5=cont6=0
    for dado in range(x):
        cont = giradas()
        if cont == 1:
            cont1+=1
        if cont == 2:
            cont2+= 1
        if cont == 3:
            cont3+=1
        if cont == 4:
            cont4+=1
        if cont == 5:
            cont5+=1
        if cont == 6:
            cont6+=1
    print (f'|| O lado 1 caiu {cont1} vezes, frequência: {cont1/x*100}%')
    print (f'|| O lado 2 caiu {cont2} vezes, frequência: {cont2/x*100}%')
    print (f'|| O lado 3 caiu {cont3} vezes, frequência: {cont3/x*100}%')
    print (f'|| O lado 4 caiu {cont4} vezes, frequência: {cont4/x*100}%')
    print (f'|| O lado 5 caiu {cont5} vezes, frequência: {cont5/x*100}%')
    print (f'|| O lado 6 caiu {cont6} vezes, frequência: {cont6/x*100}%')

def game():
    x = int(input('|| Digite quantos lançamentos do dados deseja fazer: '))
    dado(x)

jogo_dado = game()