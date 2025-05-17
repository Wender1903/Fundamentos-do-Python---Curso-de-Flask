# # Informações sobre o filme
# nome = input("Digite o nome do filme/serie: ")
# anoDeLancamento = int(input("Digite o ano de lançamento: "))
# notaDeAvaliação = float(input("Digite a nota de avaliação do filme/serie: "))

# # Verifica se o filme é recomendado

# if notaDeAvaliação > 8.0 and anoDeLancamento > 2015:
#     print(f"O(a) filme/serie: {nome} é muito bom. Recomendo assisti-lo")

# else:
#     print(f"O filme {nome} ainda não conseguiu uma boa nota, se quiser pode assistir, mas pela sua nota e/ou ano de lançamento não recomendo assisti-lo")

numero1 = float(input("Digite o primerio número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input(input("Digite a operação a ser realizada (+ - * /): ")).strip()

if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 < 0:
        resultado = numero1 / numero2
    else:
        print("Erro: Divisão por Zero")
else:
    print("Operação Inválida")
    resultado = 0
    
print(f"O resultado da operação é: {resultado:.2f}")
