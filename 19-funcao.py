# 1 - Funão para imprimir uma mensagem

def bem_vindo(): 
    print("Bem vindo ao sistemas de series!")

# for i in range(10):
#   bem_vindo()

# 2 - Função para calcular a média de notas
def calcular_media():
    numero_avaliacoes = int(input("Digite quantas avaliações deseja fazer para a série: "))
    total = 0
    for i in range(numero_avaliacoes):
        nota = float(input("Digite a nota para a série: "))
        total += nota
        
    if numero_avaliacoes > 0:
        media = total / numero_avaliacoes
    else:
        media = 0
    return media


print(f"A média das avaliações da série é: {calcular_media():.2f}")

# - Função para cadastrar um serie:
def criar_serie():
    nome_da_serie = str(input("Digite o nome da série: "))
    ano_de_lancamento = int(input("Agora digite o ano de lançamento da série: "))
    nota_da_serie = float(input("Por fim, agora digite a nota dessa série: "))
    print(f"{nome_da_serie} | {ano_de_lancamento} - nota: {nota_da_serie:.2f}")

criar_serie()
criar_serie()
