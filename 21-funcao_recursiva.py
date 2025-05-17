""" 
  Fatorial de um número:
1 -> 1 * 1
2 -> 2 * 1
3 -> 3 * 2 * 1
"""

# 1 - Fatorial de um número

def fatorial(numero):
    if numero == 1:
        return 1
    else:
        return (numero * fatorial(numero - 1))
    
num = int(input("Digite o número para ver o seu fatorial: "))
print(f"O fatorial de {num} é {fatorial(num)}")

# 2 - Spma total de um número
def total_soma(num):
    if num == 1:
        return 1
    else:
        return (num + total_soma(num - 1))
    
num = int(input("Digite o número para saber a soma total dele: "))
print(f"A soma total do número {num} é {total_soma(num)}")