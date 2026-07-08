def exercicio05():
    nomes = []
    nomes.append("Maria")
    nomes.append("Ana")
    nomes.append("João")
    nomes.append("Fábio")
    print(nomes[0])
    print(nomes[1])
    print(nomes[2])
    print(nomes[3])


def exercicio06():
    frutas = []
    frutas.append(input("Digite o nome de uma fruta: "))
    frutas.append(input("Digite o nome da segunda fruta: "))
    frutas.append(input("Digite o nome da terceira fruta: "))
    print(frutas[0])
    print(frutas[1])
    print(frutas[2])


def exercicio07():
    numeros = []
    numeros.append(int(input("Digite o primeiro numero: ")))
    numeros.append(int(input("Digite o segundo numero: ")))
    numeros.append(int(input("Digite o terceiro numero: ")))
    numeros.append(int(input("Digite o quarto numero: ")))
    print(numeros[0])
    print(numeros[1])
    print(numeros[2])
    print(numeros[3])


def exercicio08():
    notas = []
    notas.append(float(input("Digite a primeira nota: ")))
    notas.append(float(input("Digite a segunda nota: ")))
    notas.append(float(input("Digite a terceira nota: ")))
    notas.append(float(input("Digite a quarta nota: ")))
    print("Vetor original: ")
    print(notas[0])
    print(notas[1])
    print(notas[2])
    print(notas[3])
    print(f"A primeira nota digitada foi: {notas[0]}")
    print(f"A ultima nota digitada foi: {notas[3]}")
    notas[1] = 10
    notas.remove(notas[2])
    print("Vetor final: ")
    print(notas[0])
    print(notas[1])
    print(notas[2])
    print("Tamanho final: " ,len(notas))
    media = (notas[0] + notas[1] + notas[2]) / len(notas)
    print(f"Media: {media}")
