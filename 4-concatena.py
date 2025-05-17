name = str(input('Digite o nome do Filme/Série: '))
year_lauch = int(input("Digite o ano de lanamento do filme ou série: "))
noteSerie = float(input("Digite a nota do Filme/Série: "))


print("Dados do FIlme")
print('==' * 5)
# Alternativa 1

# print("Nome do Filme/Serie: ",name)
# print("Ano de Lançamento: ",year_lauch)
# print("Nota da(o) Filme/Série: ", noteSerie)

# Alternativa 2 
print("Nome do Filme/Série: ", name, "\nAno de Lançamento: ", year_lauch, "\nNota do Filme/Série: ", noteSerie)


# Alternativa 3 
print(f"Nome do Filme/Série: {name}"
      f"Ano de Lançamento: {year_lauch}"
      f"Nota do Filme/Série {noteSerie}"
)
