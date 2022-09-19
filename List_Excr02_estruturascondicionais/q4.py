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