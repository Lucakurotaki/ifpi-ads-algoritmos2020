# Entrada
print ('Bem-vindo a ferramenta de soma de centenas, dezenas e unidades!')
numero = int(input ('Digite um número de 3 dígitos: '))

# Processamento
centenas = numero // 100
dezenas = (numero - centenas * 100) // 10
unidades = numero - (centenas * 100 + dezenas * 10)
soma = centenas + dezenas + unidades

# Saída
print ('A soma dos 3 dígitos é: ', soma)