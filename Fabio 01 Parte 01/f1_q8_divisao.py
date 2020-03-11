# Entrada
print ('Este programa irá calcular a divisão da soma e diferença de 2 números que inserir')
numero1 = float(input ('Digite o primeiro número: '))
numero2 = float(input ('Digite o segundo número: '))

# Processamento
soma = numero1 + numero2
diferenca = numero1 - numero2
divisao = soma / diferenca

# Saída
print ('O resultado da divisão é: %.2f' %divisao)