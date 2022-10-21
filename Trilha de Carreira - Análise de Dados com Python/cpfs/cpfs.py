def main():
    cpfs = ["111.111.111-11", "222.222.222-22", "333.333.333-33", "111.111.111-11", "999.999.999-99", "555.555.555-55", "444.444.444-4", "000.000.000-00", "333.333.333-33"]
    cpfs_validos = limpar(cpfs)
    cpfs_ordenados = ordenar(cpfs_validos)
    print(type(cpfs_ordenados), cpfs_ordenados)

# Remover pontos e traços, CPFs duplicados e CPFs que não possuem 11 dígitos
def limpar(lista):
    lista = [elemento.replace(".", "").replace("-", "") for elemento in lista]
    lista = [elemento for elemento in lista if len(elemento) == 11]
    lista = list(set(lista))
    return lista

# Ordenar os CPFs pelo método merge_sort
# Dividir a lista original em listas menores 
def ordenar(lista):
    if len(lista) <= 1:
        return lista
    else:
        meio = len(lista) // 2
        esquerda = ordenar(lista[:meio])
        direita = ordenar(lista[meio:])
        return mesclar(esquerda, direita)

# Mesclar (em ordem) as listas
def mesclar(esquerda, direita):
    ordenada = []
    topo_esquerda, topo_direita = 0, 0
    while topo_esquerda < len(esquerda) and topo_direita < len(direita):
        if esquerda[topo_esquerda] < direita[topo_direita]:
            ordenada.append(esquerda[topo_esquerda])
            topo_esquerda += 1
        elif direita[topo_direita] < esquerda[topo_esquerda]:
            ordenada.append(direita[topo_direita])
            topo_direita += 1
    ordenada += esquerda[topo_esquerda:]
    ordenada += direita[topo_direita:]
    return ordenada

if __name__ == "__main__":
    main()