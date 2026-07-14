from typing import Dict

def exemplo_revisao():
    celular: Dict[str, str|float|int|bool] = {}
    celular["modelo"] = "Samsung A03"
    celular["armazenamento"] = 256
    celular["preco"] = 999.90
    celular["lancado"] = True

    print("celular: ",celular["modelo"])


def exercicio01():
    paciente: Dict[str, str|int]= {}

    paciente["nome_paciente"] = "Adolf"
    paciente["idade"] = 15

    print("paciente: ", paciente["nome_paciente"])
    print("Idade do paciente: ", paciente["idade"])


def exercicio02():
    aluno: Dict[str, str|int]= {}

    aluno["nome"] = "Fábinho"
    aluno["idade"] = 17
    aluno["turma"] = "DS 301"
    aluno["curso"] = "Desenvolvimento de Sistemas"
    
    for chave in aluno.keys():
        print(chave)


def exercicio03():
    produto: Dict[str, str|int|float] = {}

    produto["nome"] = "Arroz"
    produto["preco"] = 15.5
    produto["estoque"] = 5
    produto["categoria"] = "Alimento"

    for valor in produto.values():
        print(valor)
    

def exercicio04():
    funcionario: Dict[str, str|int|float] = {}

    funcionario["nome"] = "João Carlos"
    funcionario["cargo"] = "Professor"
    funcionario["salario"] = 3000.00
    funcionario["setor"] = "Tecnologia"

    for itens in funcionario.items():
        print(itens)


def exercicio05():
    livro: Dict[str, str|int|float] = {}

    livro["nome"] = input("Digite o nome do livro: ")
    livro["autor"] = input("Digite o nome do autor do livro: ")
    livro["ano"] = input("Digite o ano de publicação do livro: ")
    livro["quantidade"] = input("Digite a quantidade de páginas: ")

    for intens in livro.items():
        print(intens)


def exercicio06():
    numero = 1
    jogos: List[str, str|int|float] = [
        {
            "nome_jogo": "Read red redepution 2",
            "genero": "Ação",
            "ano_lancamento": 2015,
            "preco": 3500
        },
        {
            "nome_jogo": "God of war",
            "genero": "Ação",
            "ano_lancamento": 2025,
            "preco": 36767
        }
    ]
    for i in jogos:
        print(f" Jogo {numero}: {i}")
        numero += 1


def exercicio07():
    produtos: List[str, str|int|float] = [
        {
            "id": 4645,
            "nome": "Omo",
            "categoria": "Limpeza",
            "preco": 45.55,
            "estoque": 10
        },
        {
            "id": 54872,
            "nome": "Boneca",
            "categoria": "Brinquedo",
            "preco": 54.4542,
            "estoque": 20
        },
        {
            "id": 6776,
            "nome": "garfo",
            "categoria": "domestico",
            "preco": 6.32,
            "estoque": 200
        },
        {
            "id": 6546,
            "nome": "Carrinho",
            "categoria": "Brinquedo",
            "preco": 54.09,
            "estoque": 30
        },
        {
            "id": 6454,
            "nome": "Arroz",
            "categoria": "Alimento",
            "preco": 35.00,
            "estoque": 60
        }
    ]


def obter_nomes_produtos(produtos: Dict[str, str|int|float]):
    nomes = []
    for obter_nomes in produtos.keys():
        nomes.append(obter_nomes)
    return nomes
obter_nomes_produtos()