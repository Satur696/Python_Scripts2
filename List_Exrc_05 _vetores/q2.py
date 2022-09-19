idade = []
altura = []
media = 0
cc = 0

for a in range(1, 31):
    anos = int(input(f"Digite a idade do {a}º aluno: "))
    alt = float(input(f"Digite a altura do {a}º aluno: "))
    idade.append(anos)
    altura.append(alt)
    media += alt

media_def = (media)/30

if anos >= 13 and alt < media_def:
    cc += 1
print("--"*30)
print(f"\nNa matriz temos: \nAltura dos alunos = {altura}\nIdade dos alunos = {idade}\nA quantidade de alunos com mais de 13 anos que possuem altura inferior a média dos alunos = {cc}")