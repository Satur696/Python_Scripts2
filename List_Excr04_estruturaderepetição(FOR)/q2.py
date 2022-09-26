gabarito = ''
gabarito2 = ''
contar = 0
total_acertos = 0
total = 0
contar2 = 0
maior = 0
menor = 0
media = 0


for g in range(1,11):
    gabarito = input(f"{g} - Digite o gabarito das questões da prova (professor): ")
    gabarito2 += (gabarito)

print(">>"*30)
continuar = 'Y'
while continuar not in 'N':

    total_acertos = 0

    for p in range(1,11):
        resposta = input(f"{p} - Respostas da questões da prova (aluno): ")
        if p == 1 and resposta == gabarito2[0]:
            contar += 1
            total_acertos += 1
        elif p == 2 and resposta == gabarito2[1]:
            contar += 1
            total_acertos += 1
        elif p == 3 and resposta == gabarito2[2]:
            contar += 1
            total_acertos += 1
        elif p == 4 and resposta == gabarito2[3]:
            contar += 1
            total_acertos += 1
        elif p == 5 and resposta == gabarito2[4]:
            contar += 1
            total_acertos += 1
        elif p == 6 and resposta == gabarito2[5]:
            contar += 1
            total_acertos += 1
        elif p == 7 and resposta == gabarito2[6]:
            contar += 1
            total_acertos += 1
        elif p == 8 and resposta == gabarito2[7]:
            contar += 1
            total_acertos += 1
        elif p == 9 and resposta == gabarito2[8]:
            contar += 1
            total_acertos += 1
        elif p == 10 and resposta == gabarito2[9]:
            contar += 1
            total_acertos += 1
                
        if p == 10:
            print(">>"*30)
            continuar = input("Quer continuar como outro aluno?\n Digite [Y] para fazer a prova novamente, ou [N] para sair ")
            total+=1

        if total_acertos > maior:
            maior = total_acertos
        if total_acertos < menor or total_acertos == 1:
            menor = total_acertos
        
nota = 10*total_acertos/10
media += nota
media /= total

print(">>"*30)
print("Gabarito da Prova")
for a in gabarito2:
    contar2+=1
    print(f"{contar2} - {a}")
print(">>"*30)

print(f"Media da turma: {media}")
print(f"Maior acerto {maior}")
print(f"Menor acerto: {menor}")
print(f"Total de alunos que utilizou o sistema: {total}")