serieDict = {"serie": "Ayrthon Senna", 
             "ano de lançamento": 2025, 
             "avaliaçao": 9.8,
             "genero": ["Corrida", " Motivacional"]}

print(serieDict)
print(len(serieDict))
print(type(serieDict))

# 1 - Recuperar um elemento do dicionário
print(serieDict["serie"])
print(serieDict.get("ani de lançamento"))

# 2 - Buscar apenas as chaves do dicionário
print(serieDict.keys())

# 3 - Buscar os valores do dicionário
print(serieDict.values())

# 4 - Buscar itens do dicionário com chave e valor
print(serieDict.items())

# 5 - Adicionar itens no dicionário
serieDict["temporadas"] = 1
print(serieDict)

# 6 - Atualizar itens no dicionário
serieDict.update({"avaliaçao": 10})
print(serieDict)

# 7 - Remover item no dicionário
serieDict.pop("avaliaçao")
print(serieDict)
