#Entrada

idade = int(input("Digite a idade me dias: "))

#Processamento

anos = idade//365
meses = (idade%365)//30
dias = idade%30

#Saída

print("\nA idade de {} dias em anos, meses e dias é:\n{} anos, {} meses e {} dias.".format(idade,anos,meses,dias))
