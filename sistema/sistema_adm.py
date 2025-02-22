from sistema.repositorios.banco_de_dados import BancoDados


class Sitema_Adm:
    def __init__(self, banco_de_dados: BancoDados):
        self.banco_de_dados = banco_de_dados
        self.sessao: bool = False
             
    def executar(self):
        self.sessao = True
        while self.sessao: 
        
            print('Menu de Ações')
            print('1 - Cadastrar Veículo')
            print('2 - Remover Veículo')
            print('3 - Frota de Veículos')
            print('4 - Pesquisar um Veículo')
            print('5 - Pesquisar um Aluguel')
            print('6 - Alugueis de um Cliente') 
            print('7 - Relatório')
            print('8 - Finalizar Dia')
            print('9- Finalizar Sessão')
            print()

            verificacao = False
            while not verificacao:
                op = int(input("Escolha a ação que deseja realizar: "))
                verificacao = self.verifica_op(op)
            self.operacao(op)
    
    def operacao(self, op):
        if op == 1:
            self.cadastar_veiculo()
        elif op == 2:
            self.remover_veiculo()
        elif op == 3:
            self.frota_veiculos()
        elif op == 4:
            self.pesquisar_veiculo()
        elif op == 5:
            self.pesquisar_aluguel()
        elif op == 6:
            self.alugueis_cliente()
        elif op == 7:
            self.relatorio()
        elif op == 8:
            self.finalizar_dia()
        elif op == 9:
            self.finalizar_sessao()
        

    def cadastar_veiculo(self):
        print('Cadastrar Veículo')
        print()
        placa = input('Digite a placa do veículo: ').upper().strip()
        marca = input('Digite a marca do veículo: ').title().strip()
        modelo = input('Digite o modelo do veículo: ').title().strip()
        ano = int(input('Digite o ano do carro: '))
        valor_diaria = float(input('Digite o valor da diária: R$ '))
        self.banco_de_dados.adicionar_veiculos(placa, marca, modelo, ano, valor_diaria)
        print('Veículo Cadastrado com sucesso!')
        print()

    def remover_veiculo(self):
        placa = input('Digite a placa do veiculo: ')
        removido = self.banco_de_dados.remover_veiculo(placa)
        if not removido:
            print('Não é possível remover, pois este veículo não faz parte da frota')
        else:
            print('Veículo removido com sucesso!')
        
    def frota_veiculos(self):
        for i, veiculo in enumerate(self.banco_de_dados.lista_veiculos()):
            print(f'Veículo {i + 1}:')
            veiculo.print_veiculo()
            print()

    def pesquisar_veiculo(self):
        print('Pesquisar Veículo')
        print()
        placa = input('Digite a placa do veículo: ').upper().strip()
        veiculo = self.banco_de_dados.buscar_veiculo(placa)
        if veiculo == None:
            print('Não existe veículo com essa placa')
        else:
            veiculo.print_veiculo()

    def pesquisar_aluguel(self):
        print('Pesquisar Aluguel')
        print()
        cpf = int(input('Digite o CPF: '))
        cliente = self.banco_de_dados.buscar_cliente(cpf)
        if cliente == None:
            print('Não tem cliente com esse CPF.')
            return
        placa = input('Digite a placa: ')
        veiculo = self.banco_de_dados.buscar_veiculo(placa)
        if veiculo == None:
            print('Não tem carro com essa placa.')
            return
        aluguel = self.banco_de_dados.buscar_aluguel(cliente, veiculo)
        if cliente == None:
            print('Não tem aluguel desse veículo por este cliente.')
            return
        cliente.print_cliente()
        aluguel.print_aluguel()

    def alugueis_cliente(self):
        print('Alugueis de um Cliente')
        print()
        cpf = int(input('Digite o CPF: '))
        cliente = self.banco_de_dados.buscar_cliente(cpf)
        alugueis_cliente = self.banco_de_dados.buscar_alugueis_cliente(cliente)
        cliente.print_cliente()
        self.print_alugueis(alugueis_cliente)

    def relatorio(self):
        print()
        print('Relatório do Dia')
        print()
        print('Alugueis')
        print(f'- Total: {len(self.banco_de_dados.lista_alugueis())} alugueis')
        print()
        self.print_alugueis(self.banco_de_dados.lista_alugueis())
        print('Receita')
        print(f'- Total: R$ {self.banco_de_dados.receita():.2f}')
        print()
    
    def finalizar_dia(self):
        self.relatorio()
        self.banco_de_dados.finalizar_dia()
        print('Dia finalizado com sucesso.')

    def finalizar_sessao(self):
        print()
        print('Sessão finalizada.')
        self.sessao = False

    def print_alugueis(self, alugueis):
        for i, aluguel in enumerate(alugueis):
            print(f'Aluguel {i + 1}:')
            print(f'CPF: {aluguel.cliente.cpf}')
            aluguel.print_aluguel()
            print()

    def verifica_op(self, op):
        while op > 9 or op < 1:
            print('*OPERAÇÃO  INEXISTENTE*')
            return False
        while (op == 6) and len(self.banco_de_dados.lista_clientes()) == 0:
            print('*NÃO HÁ CLIENTES CADASTRADOS*')
            return False
        while (op == 2 or op == 3) and len(self.banco_de_dados.lista_veiculos()) == 0:
            print('*NÃO HÁ VEÍCULOS CADASTRADOS*')
            return False
        while op == 5 and len(self.banco_de_dados.lista_alugueis()) == 0:
            print('*NÃO HÁ ALUGUEIS CADASTRADOS*')
            return False
        return True    