#Entrada

nota1 = float(input("Digite a primeira nota: "))
peso1 = float(input("Digite o peso da primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
peso2 = float(input("Digite o peso da segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
peso3 = float(input("Digite o peso da terceira nota: "))

#Processamento

media = (nota1*peso1+nota2*peso2+nota3*peso3)/(peso1+peso2+peso3)

#Saída

print("A média ponderada das notas é: %.1f" %media)
