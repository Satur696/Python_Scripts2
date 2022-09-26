def celsius ():
    temp = float(input("|| Digite o valor da temperatura (ºC): "))
    return temp

def conv (temp_c):
    fahrenheit = (9*temp_c+160)/5
    return fahrenheit

def retorno(fahrenheit):
    print(f'|| A temperatura em (F) é: {fahrenheit}')

temp_c = celsius()
temp_f = conv(temp_c)
retorno(temp_f)