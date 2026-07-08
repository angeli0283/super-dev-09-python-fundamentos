def exercicio01():
    for i in range(5):
        print("Bem vindo!!")



def exercicio02():
    for i in range(15 ,31):
        print(i)



def exercicio03():
    numero = int(input("Digite um numero: "))
    #resultado = 0
    for i in range(1,11):
        #resultado = numero * i
        #print(f"{numero} X {i} = {resultado}")
        print(f"{numero} X {i} = {numero * i}")


def exercicio04():
    soma = 0
    for i in range(1,6):
        numero = int(input(f"Digite o {i}° numero:"))
        soma += numero
    print(f"Soma total: {soma}")
