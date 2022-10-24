# Questão 6
# Escreva uma função que receba as dimensões de uma fotografia em centímetros (por exemplo 10 x 15 cm) 
# e a densidade de píxeis da impressora (por exemplo 300 dpi), e retorne a resolução 
# (por exemplo 2.1 mega píxeis) mínima necessária para imprimir aquela foto. A densidade de píxeis 
# da impressora diz quantos píxeis são impressos a cada polegada. Por exemplo: 300 dpi 
# (dots per inch, ou pontos por polegada) significa que em uma polegada em linha reta da imagem há 300 
# píxeis. 

polegada = 2.54 #1 polegada equivale a 2,54 cm

def receber ():
  a = float(input('> Digite a largura/altura da fotografia (em cm): '))
  c = float(input('> Digite o comprimento da fotografia (em cm): '))
  dpi = float(input('> Digite a densidade de píxeis da impressora (por exemplo 300 dpi): '))
  return a, c, dpi

def convertor (a, c, dpi, polegada):
  pixels = dpi/polegada
  a_pixel = a*pixels
  c_pixel = c*pixels
  resolucao_megapixel = (a_pixel*c_pixel)/1000000
  print(f'> A resolução da fotografia em megapixeis é igual a {round(resolucao_megapixel, 1)} mega píxeis')

altura, comprimento, densidade = receber()
teste = convertor(altura, comprimento, densidade, polegada)