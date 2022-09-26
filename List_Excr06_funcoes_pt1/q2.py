def ler ():
    tempo = float(input('|| Digite o tempo de viagem: '))
    velocidade = float(input('|| Digite a velocidade média percorrida na viagem: '))
    return tempo, velocidade

def calc_d (tempo, velocidade):
    distancia = tempo*velocidade
    return distancia

def litro_usado (distancia):
    litros = distancia/12
    return litros

def show (distancia, litros, tempo, velocidade):
    print(f'\n|| Velocidade: {velocidade}')
    print(f'|| Tempo de viagem: {tempo}')
    print(f'|| Distância percorrida: {distancia}')
    print(f'|| Litros consumidos: {litros}')

t, v = ler()
distancia_viagem = calc_d(t, v)
litros_consumido = litro_usado(distancia_viagem)
show(v, t, distancia_viagem, litros_consumido)