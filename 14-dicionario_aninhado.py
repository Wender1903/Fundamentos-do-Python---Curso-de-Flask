import pprint

serieDict = {

    "Ayrthon Senna": {
        "ano de lançamento": 2025, 
        "avaliaçao": 9.8,
        "genero": ["Corrida", " Motivacional"]
    },
    "Interstellar": {
        "ano de lançamento": 2014, 
        "avaliaçao": 9.7,
        "genero": ["Sci-fi", " Drama"]
    },
    
    "Vingatores 4": {
        "ano de lançamento": 2019, 
        "avaliaçao": 9.7,
        "genero": ["Ação", "Comédia"]
    }
}

print(serieDict)

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(serieDict)


# 1 - Buscar informação dentro de um dicionário aninhado
print(serieDict["Ayrthon Senna"]["genero"])

# 2 - Adicionar novo item 
serieDict["Ayrthon Senna"]["plataforma de streeming"] = "Netflix"
print(serieDict["Ayrthon Senna"])

# 3 - Excluir um dicionário
del serieDict["Vingatores 4"]
pp.pprint(serieDict)
