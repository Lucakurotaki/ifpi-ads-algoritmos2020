# Entrada
numero = int(input ('Insira um número inteiro de 3 dígitos: '))

# Processamento
centenas = numero // 100
dezenas = (numero - centenas * 100) // 10
unidades = numero - (centenas * 100 + dezenas * 10)
inverso = unidades * 100 + dezenas * 10 + centenas

# Saída
print ('O inverso do número é: ', inverso)