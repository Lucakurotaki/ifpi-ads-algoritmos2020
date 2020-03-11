#Entrada

salario = float(input("Digite o salário: "))

#Processamento

aumentado = salario+salario*25/100

#Saída

print("O salário de R${:.2f} aumentado em 25% é: R${:.2f}".format(salario,aumentado))
