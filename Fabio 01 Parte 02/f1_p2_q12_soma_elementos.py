#Entrada

numero = input("Digite um número de 4 dígitos: ")

#Processamento

elemento1 = int(numero[0])
elemento2 = int(numero[1])
elemento3 = int(numero[2])
elemento4 = int(numero[3])

soma = elemento1+elemento2+elemento3+elemento4

#Saída

print("\nA soma dos elementos do número {} é:\n{}+{}+{}+{}={}".format(numero,elemento1,elemento2,elemento3,elemento4,soma))
