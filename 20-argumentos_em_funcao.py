# 1 - Função para imprimir um nome completo

def nome_completo(nome, sobrenome):
    print(f"Nome é: {nome} {sobrenome}")
    
nome_completo("Wender", "da Silva Santos")

# 2 - Função para somar 2 números
def soma(numero1, numero2):
    return numero1 + numero2

print(f"A soma é: {soma(7, 5)}")

# 3 - Função com parâmetro default

def endereço(pais="Brasil"):
    print(f"Eu moro no {pais}")
    
endereço("Brasiiillllllll")

# 4 - Função para avaliar um filme

def nota_serie(numero_avaliacoes, serie_nome):
    total = 0
    for i in range(numero_avaliacoes):
        nota = float(input(f"Digite a nota para a série {serie_nome.title()}: "))
        total += nota
    
    if numero_avaliacoes > 0:
        media = total / numero_avaliacoes
    else:
        media = 0
    
    print(f" A média de nota das avaliações da série {serie_nome.title()} é: {media:.2f}")
    
nota_serie(2, "ayrthon senna")
