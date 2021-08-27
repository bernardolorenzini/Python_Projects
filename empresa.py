class Funcionario:
    id = 0
    def __init__(self, nome, sobrenome, idade, data_entrada):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.data_entrada = data_entrada


class Gerente(Funcionario):
    juros = 800
    def __init__(self, nome, sobrenome, idade, data_entrada, salario, setor, cargo):
        super().__init__(nome, sobrenome, idade, data_entrada)
        self.salario = salario
        self.setor = setor
        self.cargo = cargo

    def pagamento(self):
        return self.salario - Gerente.juros


f1 = Funcionario("Ademir", "Silva", 55, "23/04/1992")
g1 = Gerente("Ademir", "Silva", 55, "23/04/1992", 3000, "cont", "adm" "pesq")

print(g1.pagamento())
