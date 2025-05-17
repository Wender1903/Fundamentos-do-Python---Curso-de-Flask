# Função de potência de um número

poder = lambda num: num ** 2

# Funão que verifica se o número é par
e_par = lambda x: x % 2 == 0 

# Função que divide um número por outro
dividir_numero = lambda x, y: x / y

# Função que inverte uma string
reverter_string = lambda s: s[::-1]

print(poder(7))
print(poder(9))

print(e_par(7))
print(e_par(12))

print(dividir_numero(14, 2))
print(dividir_numero(12, 4))

print(reverter_string("Python"))
print(reverter_string("Flask"))

# Funcionalidades relacionadas às Séries

series_lista = ["Ayrthon Senna", "Brooklyn 99", "Suits", "The Oficce", "É Comum Não Ser Normal"]

avaliacoes = {
    "Ayrthon Senna": [9.0, 8.7, 10.0, 9.7, 9.6],
    "Brooklyn 99": [8.0, 7.7, 9, 8.7, 8.6],
    "Suits": [9.2, 8.8, 9.0, 9.72, 9.68],
    "The Oficce": [9.75, 8.25, 8.5, 7.5, 6.5],
    "É Comum Não Ser Normal": [9.8, 9.2, 9.5, 9.5, 9.3]
    
}

# Função para calcular a média de avaliações de um filme
media_das_avaliacoes = lambda serie_nome: sum(avaliacoes[serie_nome]) / len(avaliacoes[serie_nome])


print("-=-" * 20)

print(f"A média de avaliação da Série Ayrthon Senna é de: {media_das_avaliacoes('Ayrthon Senna'):.2f}")
print(f"A média de avaliação da Série Brooklyn 99 é de: {media_das_avaliacoes('Brooklyn 99'):.2f}")
print(f"A média de avaliação da Série Suits é de: {media_das_avaliacoes('Suits'):.2f}")
print(f"A média de avaliação da Série É Comum Não Ser Normal é de: {media_das_avaliacoes('É Comum Não Ser Normal'):.2f}")

print('-=-' * 20)
# Função que verifica se uma série está na lista
verificar_serie = lambda serie_nome: serie_nome in series_lista
print(f"Ayrthon Senna está na lista? {verificar_serie('Ayrthon Senna')}")

# Função para recomendar uma série com base na avaliação média
recomendar_serie = lambda serie_nome: f"Recomendo assistir {serie_nome} com média de {media_das_avaliacoes(serie_nome):.2f}"
print(f"{recomendar_serie('Ayrthon Senna')}")
