serieLisit = ["Ayrthon Senna", "Brooklyn 99", "Suits", "The Oficce"]

# 1 - Iterando valores de uma lista de filmes usando while
indice = 0
while indice < len(serieLisit):
    print(serieLisit[indice])
    indice += 1
    
# 2 - Quando a condição for atendida, o Loop será encerrado
indice = 0
print('-=-' * 20)
while indice < len(serieLisit):
    if serieLisit[indice] == "Suits":
        break
    print(serieLisit[indice])
    indice += 1
    
# 3 - Quando a condição for atendida, o loop vai para a próxima iteração
indice = 0
print('-=-' * 20)
while indice < len(serieLisit):
    if serieLisit[indice] == "Suits":
        indice += 1
        continue
    print(serieLisit[indice])
    indice += 1
    
# 4 - Avaliação do filme com while
print('-=-' * 20)
serieNome = input("Digite o nome da Série: ")
serieAvaliacoes = int(input("Digite quantas avaliações você deseja fazer: "))
total = 0 
contador = 0

while contador < serieAvaliacoes:
    nota = float(input("Digite a nota para o filme: "))
    total += nota
    contador += 1
if serieAvaliacoes > 0:
    resultado = total / serieAvaliacoes
else:
    resultado = 0
print('-=-' * 20)
print(f"A média das avaliações da Série {serieNome} é: {resultado:.2f}")
