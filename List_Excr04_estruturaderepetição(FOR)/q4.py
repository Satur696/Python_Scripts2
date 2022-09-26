num = 1

print("Os números divisíveis por 11 entre 1000 e 1999 são:")
for num in range(999, 2000):
    if num%11 == 5:
        print(num)