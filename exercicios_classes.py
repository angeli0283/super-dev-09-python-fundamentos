import os
from typing import Dict, List

class Tenis:
    def __init__(self, modelo: str, tamanho: int, marca: str, valor: float):
        self.modelo = modelo
        self.tamanho = tamanho
        self.marca = marca
        self.valor = valor


    def apresentar(self):
        print(f"""Tenis: {self.modelo}
Marca: {self.marca}
Tamanho: {self.tamanho} 
Valor: {self.valor}
""")

def exercicio1_Tenis():
    vans = Tenis(" Old Skool", 35, "Vans", 379.99)
    nike = Tenis(" Revolution", 44,"Nike", 249.99)
    adidas = Tenis("Campus 00s", 36,"Adidas", 699.99)

    vans.apresentar()
    nike.apresentar()
    adidas.apresentar()


class Aluno:
    def __init__(self, nome: str, nota1: float, nota2: float):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    
    def apresentar_dados(self):
        print(f"""Nome do aluno: {self.nome}
Nota 1: {self.nota1}
Nota 2: {self.nota2} 
""")
        
    def calcular_media(self):
        soma = self.nota1 + self.nota2
        media = soma / 2
        print(f"A média final do aluno é: {media}")
    
    def apresentar_situacao(self):
        soma = self.nota1 + self.nota2
        media = soma / 2
        if media >= 7:
            print("Aprovado")
        else:
            print("Reprovado")

def exercicio2_aluno():
    aluno1 = Aluno("Adenor", 7.5, 8.5)
    aluno2 = Aluno("Gracyanne", 10, 10)
    aluno3 = Aluno("Regis", 5.5, 1.5)

    aluno1.apresentar_dados()
    aluno1.calcular_media()
    aluno1.apresentar_situacao()

    aluno2.apresentar_dados()
    aluno2.calcular_media()
    aluno2.apresentar_situacao()

    aluno3.apresentar_dados()
    aluno3.calcular_media()
    aluno3.apresentar_situacao()
    

class Triangulo:
    def __init__(self, base: float, altura: float, lado1: float, lado2: float, lado3: float):
        self.base = base
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def apresentar_dados(self):
        print(f"""Base: {self.base}
Altura: {self.altura}
Lado 1: {self.lado1} 
Lado 2: {self.lado2}
Lado 3: {self.lado3}
""")
        
    def calcular_area(self):
        area = (self.base * self.altura) / 2
        print(f"Área do triangulo: {area}")

    def verificar_equilatero(self):
        if self.lado1 == self.lado2 and self.lado1 == self.lado3:
            print("Esse triângulo é um triangulo Equilátero!! ")



#class Quadrado:

#class Retangulo:

#class Circulo:

