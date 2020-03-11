#Entrada

anos = int(input("Digite o número de anos que fuma: "))
cig_dia = int(input("Digite o núemero de cigarros fumados por dia: "))
carteira = float(input("Digite o valor de uma carteira de cigarro: "))

#Processamento

qtd_cig = cig_dia*anos*365
qtd_crt = qtd_cig//20 + 1
gasto = qtd_crt*carteira

#Saída

print("\nO gasto total com cigarros em {} anos é de R${:.2f}.".format(anos,gasto))
