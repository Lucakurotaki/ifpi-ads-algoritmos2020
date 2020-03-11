#Entrada

valor = float(input("Digite o valor do produto: "))

#Processamento

prestacao = valor//3
entrada = valor - prestacao*2

#Saída

print("A compra do produto será feita com entrada de R${:.2f} e duar prestações de R${:.2f}.".format(entrada,prestacao))

