def recive():
    n1 = float(input('|| Digite o primeiro número: '))
    n2 = float(input('|| Digite o segundo número: '))
    n3 = float(input('|| Digite o terceiro número: '))
    return n1, n2, n3

def maior(n1, n2, n3):
    max = n1
    if n2 > max:
        max = n2
    if n3 > max:
        max = n3
    return max

def menor(n1, n2, n3):
    min = n1
    if n2 < min:
        min = n2
    if n3 < min:
        min = n3
    return min

def show(max, min):
    print(f'O maior número é: {max}')
    print(f'O menor número é {min}')

num1, num2, num3 = recive()
maior_num = maior(num1, num2, num3)
menor_num = menor(num1, num2, num3)
show(maior_num, menor_num)