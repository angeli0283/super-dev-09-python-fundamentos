def exercicio09():
    nomes = []
    nomes.append("Maria")
    nomes.append("Ana")
    nomes.append("João")
    nomes.append("Fábio")
    nomes.append("Cristian")
    for i in nomes:
        print(i)


def exercicio10():
    frutas = []
    for i in range(5):
        frutas.append(input("Digite uma fruta: "))
    for i in frutas:
        print(i)


def exercicio11():
    numeros = []
    soma = 0
    for i in range(5):
        numeros.append(int(input("Digite um numero: ")))
    for i in numeros:
        soma += i
        print(f"numeros digitados: {i}")
    print(f"Soma total: {soma}")


def exercicio12():
    numeros = []
    soma = 0
    for i in range(6):
        numeros.append(int(input("Digite um numero: ")))
    for i in numeros:
        if i % 2 == 0:
            soma += 1
        print(f"Numeros digitados: {i}")
    print(f"Qunatidade de numeros pares: {soma}")


def exercicio13():
    notas = []
    soma = 0
    for i in range(4):
        notas.append(float(input("Digite a nota: ")))
    for i in notas:
        soma += i
        print(f"Notas digitadas: {i}")
        media = soma / len(notas)
    print(f"Media final: {media}")
    if media >= 7:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")
exercicio13()