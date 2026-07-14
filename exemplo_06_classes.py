class Cachorro:
    #_init_é o construtor da classe, que é executado
    #quando instanciamos um objeto da classe
    def _init_(self, apelido: str,raca: str, cor: str, peso: float, idade: int):
        self.apelido = apelido
        self.raca