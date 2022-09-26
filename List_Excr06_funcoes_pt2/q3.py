def recive():
    n = int(input('|| Digite um número inteiro e positivo: '))
    return n

def primo(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(f'{n} não é primo.')
                break
        else:
            print(f'{n} é primo.')
    elif n == 0:
        print('Zero é neutro.')

num = recive()
primo_numero = primo(num)