n1 = 0
n2 = 0
n3 = 0


for aluno in range(1, 51):
    n1 = float(input("Digite a primeira nota do aluno: "))
    n2 = float(input("Digite a segunda nota do aluno: "))
    n3 = float(input("Digite a terceira nota do aluno: "))
    mp = (n1*2+n2*3+n3*4)/10
    print(f"A média ponderada da nota do {aluno}º aluno é: {mp}")