#Entrada

numero = int(input("Digite um número de 3 dígitos: "))

#Processamento

centena = numero//100
dezena = (numero%100)//10
unidade = numero%10

inverso = unidade*100+dezena*10+centena

diferenca = numero-inverso

#Saída

print("\nO inverso de {} é {}".format(numero,inverso))
print("A diferença entre {} e {} é {}.".format(numero,inverso,diferenca))
