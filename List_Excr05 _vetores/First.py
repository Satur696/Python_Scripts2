from msilib.schema import ReserveCost


print('\n')
anarchy = ['rage', 'love', 'death', 'loyalty', 'hope', 'war', 'treat', 'vengeance', 'simpathy', 'euphoria']
print(type(anarchy)) # Tipo de lista
print(anarchy[0]) # O Index (ID) de um elemento na lista começa por 0
print(anarchy[-2]) # O sinal negativo inverte a ordem do index, logo -1 é o último item e -2 é o penúltimo
print(anarchy[9-8]) # Operações aritméticas com o index funcionam (apenas número inteiro)
despair = anarchy # Compartilhando elementos de lista
print(despair)
anarchy.remove('euphoria') # Alterações feitas em uma lista principal afetarão as compartilhas
print(despair)
kindness = anarchy[:] # Utiliza-se [:] para copiar uma lista sem que alterações na principal afetem a cópia
anarchy.pop(-1) 
print(despair)
print(kindness)
respect = anarchy + kindness # juntando duas listas
print(respect)
respect += ["regret"] # Adicionando um item (pode usar append também)
print(respect)
anarchy.append('chaos')
print(anarchy)
print(anarchy.index('chaos')) # Retorna o index de um elemento na lista
print(anarchy.index('vengeance'))
anarchy.insert(1, 'wealth') # Escolha onde adicionar um elemento (index)
print(anarchy)
anarchy.remove('hope') # Remove um elemento
print(anarchy)
anarchy.pop(6) # Remove por index
print(anarchy)
anarchy.sort() # Ordem alfabética
print(anarchy)
print(sorted(kindness)) # Ordem alfabética mas no print
print(len(anarchy)) # tamanho de uma lista
for x in anarchy: # printa cada um dos elementos (percorre a lista)
    print(x)