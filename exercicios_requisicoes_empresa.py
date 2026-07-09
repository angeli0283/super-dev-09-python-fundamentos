import requests

url_base = "https://api.franciscosensaulas.com"

def consultar_empresa():
    url = f"{url_base}/api/v1/empresa" 

    resposta = requests.get(url)
    print("Status Code: ", resposta.status_code)
    print("Response: ", resposta.text)


def consultar_empresa_por_id():
    id = 150
    url = f"{url_base}/api/v1/empresa/{id}"
    resposta = requests.get(url)
    print("Status Code: ", resposta.status_code)
    print("Response: ", resposta.text)


def consultar_produtos():
    url = f"{url_base}/api/v1/empresa/produtos"
    resposta = requests.get(url)
    print("Status Code: ", resposta.status_code)
    print("Response: ", resposta.text)


def consultar_produto_por_id():
    id = 24
    url = f"{url_base}/api/v1/empresa/produtos/{id}"
    resposta = requests.get(url)
    print("Status Code: ", resposta.status_code)
    print("Response: ", resposta.text)


def cadastrar_empresa():
    url = f"{url_base}/api/v1/empresa"

    empresa = {
        "nome": "Coisa",
        "cnpj": "1132"
    }
    resposta  = requests.post(url, json=empresa)
    print("Status Code: ", resposta.status_code)
    print("dados da empresa cadastrada")
cadastrar_empresa()