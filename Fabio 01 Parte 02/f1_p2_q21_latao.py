#Entrada

qtd_latao = float(input("Digite a quantidade de latão desejada(kg): "))

#Processamento

cobre = qtd_latao*0.7
zinco = qtd_latao-cobre

#Saída

print("\nPara se obter {}kg de latão, é necessário {:.2f}kg de cobre e {:.2f}kg de zinco.".format(qtd_latao,cobre,zinco))
