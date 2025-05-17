serieName = "Ayrthon Senna"
# string [inicio/fim] - indicde começa na posição 0 / indice final - 1

# 1 - Buscar string a partir da primeira posição
print(serieName[0:])

# 2 - Buscar toda string até a última posição
print(serieName[:13])

# 3 - Buscar toda string da terceira até a ultima posição
print(serieName[2:])

""" 
string [inicio:fim:passo] 
indicde começa na posição 0 / indice final - 1 
passo - determina o incremento. Por padrão esse número é o 1
"""

# 4 - Buscar toda a string de 2 em 2 caracteres
print(serieName[::2])

# 5 - Buscar toda a string nos indices impares
print(serieName[1::2])

# 6 - Inverter uma string de trás pra frente
print(serieName[::-1])