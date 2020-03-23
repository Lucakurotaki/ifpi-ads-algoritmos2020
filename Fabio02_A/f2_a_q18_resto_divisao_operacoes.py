def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    print(resultado(num1,num2))

def resultado(n1,n2):

    if n1%n2 == 1:
        return "{}+{}+{} = {}.".format(n1,n2,1,n1+n2+1)

    elif n1%n2 == 2:
        return par_impar(n1)+par_impar(n2)

    elif n1%n2 == 3:
        return "({}+{})*{} = {}.".format(n1,n2,n1,(n1+n2)*n1)

    elif n1%n2 == 4:
        return "({}+{})/{} = {}.".format(n1,n2,n2,(n1+n2)/n2)
    
    else:
        return quadrado(n1)+quadrado(n2)

def par_impar(num):

    if num%2 == 0:
        return "{} é par.\n".format(num)
    else:
        return "{} é ímpar.\n".format(num)

def quadrado(num):

    return "{}² = {}.\n".format(num,num**2)

main()
