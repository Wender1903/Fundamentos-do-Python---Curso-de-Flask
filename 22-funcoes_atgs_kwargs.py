""" 
*args - Utilizamos ele quando não temos certeza de quantos argumentos queremos ter numa função
 - Os argumentos são passsados como uma tupla
 
 **kwargs - Além dos valores podemos passar também as respectivas chaves para cada argumento.
- Os argumentos são passsados como um dicionário 
"""

# 1 - Soma de números (para essa finalidade o ideal e que vamos usar são os *args)
def soma(*num):
    soma_total = 0
    for numero in num:
        soma_total += numero
    print(f"Soma é: {soma_total}")    
    

soma(7, 9, 7)
soma(7, 9, 7, 7, 7)

# 2 - Apresentação de curso (para essa finalidade o ideal e que vamos usar os **kwargs)
def apresentacao(**dados):
    for key, value in dados.items():
        print(f"{key} - {value}")

print("---------------- Lista de Cursos ----------------")
apresentacao(nome="Pyton", categoria="Backend", nivel="Iniciante")
apresentacao(nome="Javascript", categoria="Frontend", nivel="Intermediário")
apresentacao(nome="Flask APIs RESTFULL", categiria="Backend", nivel="Avançado")
