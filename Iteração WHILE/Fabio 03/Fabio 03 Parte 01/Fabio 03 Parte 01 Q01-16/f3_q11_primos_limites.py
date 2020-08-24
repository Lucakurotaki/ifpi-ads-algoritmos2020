#Entrada

ls = int(input("Digite o valor do limite superior: "))
li = int(input("Digite o valor do limite inferior: "))

#Processamente/Saída

if ls < li:
    print("Erro. O valor do limite superior é menor do que o valor do limite inferior.")

else:
    cont = 0
    while cont <= ls:
        if cont > li:
            if cont == 1 or cont == 2 or cont == 3 or cont == 5 or cont == 7:
                print(cont)
            elif cont%2 != 0 and cont%3 != 0 and cont%5 != 0 and cont%7 != 0:
                print(cont)
        cont+=1
