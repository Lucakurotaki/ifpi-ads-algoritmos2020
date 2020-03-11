#Entrada

dias = int(input("Digite o número de dias: "))

#Processamento

semanas = dias//7
dias_resto = dias%7

#Saída

print("{} dias equivale a {} semanas e {} dias.".format(dias,semanas,dias_resto))
