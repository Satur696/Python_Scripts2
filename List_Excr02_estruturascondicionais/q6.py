precoProduto1 = float(input("Digite o preço do primeiro produto: R$"))
precoProduto2 = float(input("Digite o preço do segundo produto: R$"))
precoProduto3 = float(input("Digite o preço do terceiro produto: R$"))

if precoProduto1 < precoProduto2:
    if precoProduto1 < precoProduto3:
        print(f"O produto 1 custa R${precoProduto1}, portanto ele é o mais barato.")
    else:
        print(f"O produto 3 custa R${precoProduto3}, portanto ele é o mais barato.")

elif precoProduto2 < precoProduto1:
    if precoProduto2 < precoProduto3:
        print(f"O produto 2 custa R${precoProduto2}, portanto ele é o mais barato.")
    else:
        print(f"O produto 3 custa R${precoProduto3}, portanto ele é o mais barato.")

else:
    print("Todos os produtos tem o mesmo valor!")