def somaImposto(taxaImposto, custo):
    r_imposto = custo + (custo*taxaImposto/100)
    return r_imposto

taxa_imposto = int(input('|| Digite a taxa de imposto sobre o item (%): '))
custo = float(input('|| Digite o custo do item: R$'))
imposto = somaImposto(taxa_imposto, custo)
print(f'|| O item vai custar: R${imposto}')