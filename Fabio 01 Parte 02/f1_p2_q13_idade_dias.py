#Entrada

idade_anos = int(input("Digite os anos da sua idade: "))
idade_meses = int(input("Digite os meses da sua idade: "))
idade_dias = int(input("Digite os dias da sua idade: "))

#Processamento

idade = idade_anos*365+idade_meses*30+idade_dias

#Saída

print("A idade, em dias é: {} dias.".format(idade))
