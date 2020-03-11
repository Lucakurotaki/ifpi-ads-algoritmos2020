#Entrada

real = float(input("Digite o valor em real: "))

#Processamento

desconto = real*70/100

#Saída

print("70% de R${:.2f} é: R${:.2f}".format(real,desconto))
