negative = 0

for n in range(1, 6):
    num = float(input("Digite o {}º: ".format(n)))
    if num < 0:
        negative += 1

print("Foram digitados {} números".format(negative))