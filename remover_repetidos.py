def remover_repetidos(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


lista = [1, 2, 2, 3, 4, 4, 10, 9, 5, 10, 5, 8, 9, 8]
print(remover_repetidos(lista))
print("O tamanho da lista original era: ", len(lista))
print("Após a remoção dos itens repetidos o tamanho é ", len(remover_repetidos(lista)))