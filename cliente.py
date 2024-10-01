class Cliente:
    def __init__(self, nome, cpf, telefone, email, cnh, senha):
        self.nome = nome
        self.cpf = cpf
        self.telefone =telefone
        self.email = email
        self.cnh = cnh
        self.senha = senha

    def print_cliente(self):
        print(f'Cliente')
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Telefone: {self.telefone}')
        print(f'E-mail: {self.email}')
        print(f'CNH: {self.cnh}')
        print()
    