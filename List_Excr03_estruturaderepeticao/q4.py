num = 1
in1 = 0
in2 = 0
in3 = 0
in4 = 0

while num > 0:
    num = int(input("Digite um número:"))
    if num >= 0 and num <= 25:
        in1 += 1
    elif num >= 26 and num <= 50:
        in2 += 1 
    elif num >= 51 and num <= 75:
        in3 += 1
    elif num >= 76 and num <= 100:
        in4 += 1

print(f"A quantidade de números no intervalo entre [0, 25]: {in1}. Entre o intervalo [26, 50]: {in2}. Entre o intervalo [51, 75]: {in3}. Entre o intervalo [76-100]: {in4}.")