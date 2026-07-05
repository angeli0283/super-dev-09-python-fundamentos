def exercicio_01_mensagens():
    print("Olá,seja bem vindo!! ")
    print("Você está aprendendo python")
    print("Python é usado para criar programas")




def exercicio_02_variaveis():
    nome = "Amanda"
    idade = 15
    cidade = "Blumenau"

    print(f"Nome: {nome}\n"
    f"Idade: {idade}\n"
    f"Cidade: {cidade}\n")


def exercicio_03_input_nome():
    nome = input("Qual é o seu nome?? ")
    print(f"Olá {nome} seja bem vindo ao sistema!! ")


def exercicio_04_dados_pessoais():
    nome = input("Escreva o seu nome: ")
    bairro = input("Digite seu bairro: ")
    cidade = input("Digite sua cidade: ")

    print(f"{nome} mora no bairro {bairro}, na cidade {cidade}.")


def exercicio_05_idade_int():
    idade = int(input("Digite sua idade: "))
    print(f"Você tem {idade} anos.")


def exercicio_06_idade_proximo_ano():
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    print(f"{nome}, no proximo ano você terá {idade + 1} anos")


def exercicio_07_dobro_numero():
    numero = int(input("Digite um numero: "))
    print(f"O dobro do {numero} é {numero * 2}")


def exercicio_08_maioridade():
    idade = int(input("Escreva a sua idade: "))
    if idade >= 18:
        print("Você é maior de idade!!")
    else:
        print("Você ainda é menor de idade")


def exercicio_09_numero_positivo():
    numero = int(input("Escreva um numero: "))
    if numero > 0 :
        print("O numero é positivo")
    elif numero == 0:
        print("O numero é Zero")
    else:
        print("O numero é negativo")


def exercicio_10_entrada_evento():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    if idade >= 16:
        print(f"{nome}, Você pode entrar no evento!!")
    else: 
        print(f"{nome}, Você não pode entrar no evento!!")


def exercicio_11_verificar_nota():
    nota = float(input("Ecreva a nota: "))
    if nota >= 7:
        print("Aluno aprovado!!")
    else: 
        print("Aluno reprovado")


def exercicio_12_verificar_saldo():
    saldo = float(input("Digite seu saldo: "))
    valor = float(input("Digite o valor da compra: "))
    if saldo >= valor:
        print("Compra aprovada")
    else:
        print("Salado insuficiente")


def exercicio_13_aprovacao_nota_frequencia():
    nota = float(input("Digite a nota: "))
    frequencia = int(input("Digite a frequência: "))
    if nota >= 7 and frequencia >= 75:
        print("Aluno aprovado.")
    else: 
        print("Aluno reprovado")


def exercicio_14_entrada_gratuita():
    idade = int(input("Escreva a sua idade: "))
    if idade < 6 or idade >= 60:
        print("Entrada gratuita")
    else:
        print("Entrada paga")


def exercicio_15_login_simples():
    usuario = input("Digite o nome de usuario: ")
    senha = input("Digite a senha: ")
    if usuario == "admin" and senha == "1234":
        print("Login realizado com suesso")
    else: 
        print("Usuario ou senha incorretos")

def exercicio_16_mensagem_varias_vezes():
    i = 1
    while i < 6:
        print("Estou aprendendo python!!")
        i += 1


def exercicio_17_numeros_pares():
    i = 2
    while i % 2 == 0 and i < 21:
        print(i)
        i += 2


def exercicio_18_repetir_mensagem():
    mensagem = input("Escreva uma mensagem: ")
    vezes = int(input("Escreva a quantidade de vezes que queira repetir: "))
    i = 0
    while i < vezes:
        print(mensagem)
        i += 1


def exercicio_19_somar_1_ate_n():
    numero = int(input("Escreva um numero inteiro: "))
    soma = 0
    i = 0 
    while i < numero:
        i += 1
        soma += i 
    print(f"A soma é {soma}")
        

def exercicio_20_senha_while():
    senha = input("Digite a senha: ")
    while senha != "1234":
        print("Senha incorreta. Tente novamente.\n")
        senha = input("Digite a senha: ")
    print("Acesso permitido.")


def exercicio_21_menu_simples():
    opcao = int(input("Escolha uma opção: \n"
        "1 - Mostrar mensagem de boas vindas\n"
        "2 - Mostrar mensagem sobre python\n"
        "0 - Sair\n"
        "Opção: "))
    while opcao != 0:
        
        if opcao == 1:
            print("Bem vindo!!\n")
        elif opcao == 2:
            print("Python é uma linguagem de programação\n")
        else: 
            print("opção inválida!!\n")
        opcao = int(input("Escolha uma opção: \n"
        "1 - Mostrar mensagem de boas vindas\n"
        "2 - Mostrar mensagem sobre python\n"
        "0 - Sair\n"
        "Opção: "))
    print("Programa encerrado")


def exercicio_22_tabuada_while():
    numero = int(input("Escreva um numero: "))
    i = 1
    resultado = 0
    while i < 11:
        resultado = numero * i
        print(f"{numero} X {i} = {resultado}")
        i += 1
    

def exercicio_23_somar_ate_zero():
    numero = int(input("Escreva um numero: "))
    contador = numero
    while numero != 0:
        numero = int(input("Escreva um numero: "))
        contador += numero
    print(f"A soma dos numeros digitados é: {contador}")


def exercicio_24_contar_positivos():
    numero = 1
    contador = 0
    while numero != 0:
        numero = int(input("Escreva um numero: "))
        if numero > 0:
            contador += 1
    print(f"Quantidade de numeros pisitivos: {contador}")


def exercicio_25_maior_numero():
    maior = 0
    i = 0
    while i < 5:
        numero = int(input("Digite um numero: "))
        if numero > maior:
            maior = numero
        i+= 1
    print(f"O maior numero digitado foi {maior}")


def exercicio_26_media_notas_while():
    i = 0
    soma = 0
    while i < 4:
        nota = int(input("Digite a nota: "))
        soma += nota
        i += 1
    media = soma / 4
    print(f"A média do aluno é: {media}")


def exercicio_27_senha_tentativas():
    i = 0
    senha = 0
    while i < 3 and senha != "1234":
        senha = input("Digite a senha: ")
        if senha != "1234":
            print("Senha incorreta\n")
        else:
            print("Acesso permitido")
        i += 1
    if i == 3 and senha != "1234":
        print("Acesso bloqueado")
        

def exercicio_28_validar_idade():
    idade = -1
    while idade < 0 or idade > 120:
        idade = int(input("Digite sua idade: "))
        if idade < 0 or idade > 120:
            print("Idade invalida.Digite novamente\n")
    print("Idade cadastrada com sucesso!!")


def exercicio_29_adivinhar_numero():
    pass