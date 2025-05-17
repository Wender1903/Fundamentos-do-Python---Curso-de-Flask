serieSet = {"Brooklyn 99", "The Oficce", "Tudo Bem não Ser Normal", "Suits", "Jovem Shelton"}

print(type(serieSet))

# 1 - Buscar o tamanho do set
print(len(serieSet))

# 2 - True e 1 são considerados o mesmo valor
exempleSet = {"Exemplo", True, 1, 8.7}
print(exempleSet)

# 3 - Adicionar item de outro set
serieSet.update(exempleSet)
print(serieSet)

# 4 - Remover um item no set
serieSet.remove(True)
serieSet.remove(8.7)
serieSet.remove("Exemplo")
print(serieSet)