#Entrada

numerador1 = int(input("Digite o valor do numerador da primeira fração: "))
denominador1 = int(input("Digite o valor do denominador da primeira fração: "))
numerador2 = int(input("Digite o valor do numerador da segunda fração: "))
denominador2 = int(input("Digite o valor do numerador da segunda fração: "))

#Processamento

den_novo = denominador1*denominador2
num_novo = numerador1*denominador2+numerador2*denominador1

#Saída

print("A soma entre {}/{} e {}/{} é: {}/{}.".format(numerador1,denominador1,numerador2,denominador2,num_novo,den_novo))
