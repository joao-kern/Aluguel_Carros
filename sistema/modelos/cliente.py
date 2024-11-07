class Cliente:
    def __init__(self, nome, cpf, telefone, email, cnh, senha) -> None:
        self.nome: str = nome
        self.cpf: str = cpf
        self.telefone: str =telefone
        self.email: str = email
        self.cnh: str = cnh
        self.senha: str = senha

    def print_cliente(self) -> None:
        print(f'Cliente')
        print(f'Nome: {self.nome}')
        print(f'CPF: {self.cpf}')
        print(f'Telefone: {self.telefone}')
        print(f'E-mail: {self.email}')
        print(f'CNH: {self.cnh}')
        print()
    