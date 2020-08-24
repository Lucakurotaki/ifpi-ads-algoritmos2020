#Entrada

num = int(input("Digite o número: "))

#Processamento

if num < 1:
    print("Digite um número maior do que 0.")

else:
    cont = num-1
    fat = num
    while cont > 1:
        fat*=cont
        cont-=1

#Saida

    print("{}! = {}".format(num,fat))
