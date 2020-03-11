# Entrada
print ('Este programa irá calcular o quociente e o resto dos dois números que inserir.')
numero1 = int(input ('Digite o primeiro número: '))
numero2 = int(input ('Digite o segundo número: '))

# Processamento
quociente = numero1 // numero2
resto = numero1 % numero2

# Saída
print ('O quociente e o resto da divisão são: {} e {}'.format (quociente, resto))