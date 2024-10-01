from sistema_adm import Sitema_Adm
from sistema_cliente import Sistema_Cliente

class Sistema:
    def __init__(self, banco_de_dados, adm):
        self.banco_de_dados = banco_de_dados
        self.adm = adm
        self.execucao = False

    def executar(self):
        self.execucao = True
        while self.execucao: 
            print('Menu de Ações')
            print('1 - Criar Conta')
            print('2 - Entrar na sua Conta - Cliente')
            print('3 - Entrar na sua Conta - Administrador')
            print('4 - Finalizar Programa')

            verificacao = False
            while not verificacao:
                op = int(input("Escolha a ação que deseja realizar: "))
                verificacao = self.verifica_op_login(op)
            self.operacao(op)

    def operacao(self, op):
        if op == 1:
            self.criar_conta()
        elif op == 2:
            self.login_conta()
        elif op == 3:
            self.login_adm()
        elif op == 4:
            self.finalizar_programa()

    def criar_conta(self):
        print('Criar Conta')
        print()
        nome = input('Nome: ').title().strip()
        cpf = int(input('CPF (sem pontuação): '))
        telefone = input('Telefone (sem espaços e pontuações): ')
        email = (input('Email: ')).lower().strip()
        cnh = int(input('CNH (sem pontuação): '))
        senha = input('Senha: ')
        self.banco_de_dados.adicionar_cliente(nome, cpf, telefone, email, cnh, senha)
        print('Conta Cadastrada com sucesso!')
        print()
            
    def login_conta(self):
        print('Login Conta - Cliente')
        print()
        cpf = int(input('CPF (sem pontuação): '))
        senha = input('Senha: ')
        login, cliente = self.verifica_login_cliente(cpf, senha)
        if login:
            print("Login realizado com sucesso!")
            sistema_cliente = Sistema_Cliente(self.banco_de_dados, cliente)
            sistema_cliente.executar()
        else:
            print("CPF ou senha incorreta!")
        print()
            
    def login_adm(self):
        print('Login Conta - Administrador')
        print()
        usuario = input('Usuário: ')
        senha = input('Senha: ')
        login= self.verifica_login_adm(usuario, senha)
        if login:
            print("Login realizado com sucesso!")
            sistema_adm = Sitema_Adm(self.banco_de_dados)
            sistema_adm.executar()
        else:
            print("Usuário ou senha incorreta!")
        print()
            
    def verifica_op_login(self, op):
        while op > 4 or op < 1:
            print('*OPERAÇÃO  INEXISTENTE*')
            return False
        return True

    def verifica_login_cliente(self, cpf, senha):
        for cliente in self.banco_de_dados.lista_clientes():
            if cliente.cpf == cpf and cliente.senha == senha:
                return True, cliente
    
        return False, None

    def verifica_login_adm(self, usuario, senha):
        if self.adm.usuario == usuario and self.adm.senha == senha:
            return True
    
        return False

    def finalizar_programa(self):
            print("Programa Finalizado")
            self.execucao = False
            