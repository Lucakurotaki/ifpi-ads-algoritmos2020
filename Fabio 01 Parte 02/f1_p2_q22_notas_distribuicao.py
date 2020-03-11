#Entrada

valor = float(input("Digite o valor de saque: "))

#Profcesamento

notas50 = valor//50
notas20 = valor%50//20
notas10 = (valor%50)%20//10
notas5 = ((valor%50)%20)%10//5
notas2 = ((((valor%50)%20)%10)%5)//2

#Saída

print("\nA distribuição das notas no saque de R${:.2f} será:"
      "\n{:.0f} notas de R$50,00;"
      "\n{:.0f} notas de R$20,00;"
      "\n{:.0f} notas de R$10,00;"
      "\n{:.0f} notas de R$5,00;"
      "\n{:.0f} notas de R$2,00.".format(valor,notas50,notas20,notas10,notas5,notas2))
