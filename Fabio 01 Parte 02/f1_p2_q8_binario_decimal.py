#Entrada

binario = input("Digite um número binário de 4 dígitos: ")

#Processamento

digito1 = int(binario[3])*2**0
digito2 = int(binario[2])*2**1
digito3 = int(binario[1])*2**2
digito4 = int(binario[0])*2**3

decimal = digito1 + digito2 + digito3 + digito4

#Saída

print("O número binário {} equivale a {} na base decimal.".format(binario,decimal))
