# 1 - Listar valores de 0 a 10 que sejam menores do que 4
listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

# Lista de Series
serieLisit = ["Ayrthon Senna", "Brooklyn 99", "Suits", "The Oficce"]

# 2- Filmes que possuem a letra 'e' no título
serieComE = [serie for serie in serieLisit if 'e' in serie.lower()]
print(serieComE)

# 3 - Mapear as séries que eu assisti
serieAssistidas = [serie for serie in serieLisit if serie != "Ayrthon Senna"]
print(serieAssistidas)

# 4 - Encontrando um filme pelo nome
while True:
    pesquisarNome = str(input("Digite o nome da série para buscarmos ele na lista (ou sair para encerrar): "))
    if pesquisarNome.lower() == 'sair':
        print("Programa encerrado")
        break
    
    seriesEncontradas = [serie for serie in serieLisit if pesquisarNome.lower() in serie.lower()]
    
    if seriesEncontradas:
        print(f"Séries encontradas com o nome: {pesquisarNome}: ")
        for serieEncontrada in seriesEncontradas:
            print(serieEncontrada)
    else:
        print(f"Nenhum Filme foi encontrado com o nome {pesquisarNome}. Tente novamente.")
    