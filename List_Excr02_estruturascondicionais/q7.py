num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
num3 = float(input("Digite o terceiro número"))

if num1 >= num2 and num2 >= num3:
    print(f"{num1}, {num2} e {num3}")

elif num2 >= num1 and num1 >= num3:
    print(f"{num2}, {num1} e {num3}")

elif num1 >= num3 and num1 >= num2:
    print(f"{num1}, {num3}, {num2}")
    
else:
    print(f"{num3}, {num2}, {num1}")