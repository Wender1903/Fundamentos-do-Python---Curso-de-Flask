serieList = ["Brooklyn 99", "The Oficce", "Tudo Bem não Ser Normal", "Suits", "Jovem Shelton"]

# 1 - Tamanho da lista
print(len(serieList))

# 2 - Recuperar um item da lista pelo nome
print(serieList.index("Brooklyn 99"))

# 3 - Adicionar item ao final da lista
serieList.append("Quando o Telefone Toca")
print(serieList)

# 4 - Ordenar uma Lista
serieList.sort()
print(serieList)

# 5 - Copiar os itens de uma lista para outra
serieCopy = serieList.copy()
serieCopy.remove("Suits")
print(serieCopy)

# 6 - Remove todos os itens da lista
serieCopy.clear()
print(serieCopy)