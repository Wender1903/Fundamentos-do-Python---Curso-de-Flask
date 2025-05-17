# Lista de Series

serieLsit = ["Ayrthon Senna", "Brooklyn 99", "Suits", "The Oficce"]

# 1 - Iterando valores de uma lista
for serie in serieLsit:
    print(serie)
    
# 2 - Quando a condição for atendida, o Loop será encerrado
for serie in serieLsit:
    if serie == "Brooklyn 99":
        break
    print(serie)
    
# 3 - Quando a condição for atendida, o Loop vai para a próxima iteração
for serie in serieLsit:
    if serie == "Brooklyn 99":
        continue
    print(serie)
    
# 4 - Avalição do filme
serieNome = input("Digite o nome da serie: ")
serieAvaliacoes = int(input("Digite quantas avaliações deseja fazer: "))

total = 0
for i in range(serieAvaliacoes):
    nota = float(input("Digite a nota para a serie: "))
    total += nota
    
if serieAvaliacoes >0:
    media = total / serieAvaliacoes
else:
    media = 0

print(f"A média das avalições da serie {serieNome} é: {media:.2f}")
    
    
    