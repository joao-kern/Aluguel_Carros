from datetime import date

class Sistema_Cliente:
    def __init__(self, banco_de_dados, cliente):
        self.banco_de_dados = banco_de_dados
        self.cliente = cliente
        self.sessao = False


    def executar(self):
        self.sessao = True
        while self.sessao: 
        
            print('Menu de Ações')
            print('1 - Realizar Aluguel')
            print('2 - Devolução Aluguel')
            print('3 - Meus Alugueis') 
            print('4 - Finalizar Sessão')
            print()

            verificacao = False
            while not verificacao:
                op = int(input("Escolha a ação que deseja realizar: "))
                verificacao = self.verifica_op(op)
            self.operacao(op)
    
    def operacao(self, op):
        if op == 1:
            self.realizar_aluguel()
        elif op == 2:
            self.devolucao_aluguel()
        elif op == 3:
            self.meus_alugueis()
        elif op == 4:
            self.finalzar_sessao()

    def realizar_aluguel(self):
            print('Realizar Aluguel')
            print()
            self.frota_veiculos()
            placa = input('Digite a placa do veículo: ').upper().strip()
            veiculo = self.banco_de_dados.buscar_veiculo(placa)
            if veiculo == None:
                print('Não tem veículo com essa placa.')               
            else:
                disponibilidade = self.banco_de_dados.verifica_status_veiculo(veiculo)
                if not disponibilidade:
                    print('O veículo já está alugado.')
                else:
                    while True:
                        data_inicio = input('Digite a data em que começa o aluguel (formato: ano-mês-dia ): ')
                        data_termino = input('Digite a data em que termina o aluguel (formato: ano-mês-dia ): ')
                        data_inicio = date.fromisoformat(data_inicio)
                        data_termino = date.fromisoformat(data_termino)
                        dias_aluguel = (data_termino - data_inicio).days
                        if dias_aluguel <= 0:
                            print('*Datas impossíveis - Data de termino menor que data de começo do aluguel*')
                            break
                        else:
                            aluguel = self.banco_de_dados.adicionar_alugueis(data_inicio, data_termino, self.cliente, veiculo)
                            print('Aluguel realizado com sucesso!')
                            print(f'Valor Total: R$ {aluguel.valor_aluguel()}') 
                            print(' ')
                            break
    
    def devolucao_aluguel(self):
        print('Devolução Aluguel')
        print()
        placa = input('Digite a placa do veículo: ').upper().strip()
        veiculo = self.banco_de_dados.buscar_veiculo(placa)
        if veiculo == None:
            print('Não tem veículo com essa placa.')
        else:
            disponibilidade = self.banco_de_dados.verifica_status_veiculo(veiculo)
            if disponibilidade == False:
                    print('O veículo não está alugado.')
            else:
                data_devolucao = input('Digite a data de devolução (formato: ano-mês-dia ): ')
                data_devolucao = date.fromisoformat(data_devolucao)
                while True:
                    danos = input('Digite se houve danos ao carro (S/N): ').strip().upper()
                    if danos == 'S' or danos == 'N':
                        aluguel = self.banco_de_dados.buscar_aluguel(self.cliente, veiculo)
                        multa = self.devolucao(aluguel, data_devolucao, danos)
                        if multa != 0 and multa != None:
                            print(f'Houve uma multa de: R$ {multa:.2f}')
                            print('Devolução realizada com sucesso!')
                            break
                        elif multa == None:
                            print('*Data de devolução impossível*\n(Menor que a data de início)')
                            print()
                            break
                        else:
                            print('Não houve multa')
                            print('Devolução realizada com sucesso!')
                            break
                        print()

    def meus_alugueis(self):
        print('Meus Alugueis')
        print()
        alugueis_cliente = self.banco_de_dados.buscar_alugueis_cliente(self.cliente)
        self.cliente.print_cliente()
        self.print_alugueis(alugueis_cliente)

    def finalzar_sessao(self):
        print()
        print('Programa Encerrado.')
        self.sessao = False
    
    def verifica_op(self, op):
        while op > 4 or op < 1:
            print('*OPERAÇÃO  INEXISTENTE*')
            return False

        return True

    def devolucao(self, aluguel, data_devolucao, danos):
        aluguel.veiculo.alterar_status('Disponível')
        if (data_devolucao - aluguel.data_inicio).days < 0:
            return None
        quilometragem_andada = float(input('Digite a quilometragem andada durante o aluguel em KM: '))
        aluguel.veiculo.alterar_quilometragem(quilometragem_andada)
        aluguel.confirmar_devolucao()
        multa = aluguel.verifica_multa(data_devolucao, danos)
        self.banco_de_dados.alterar_renda_diaria(multa)

        return multa
    
    def print_alugueis(self, alugueis):
        for i, aluguel in enumerate(alugueis):
            print(f'Aluguel {i + 1}:')
            aluguel.print_aluguel()
            print()
    
    def frota_veiculos(self):
        for i, veiculo in enumerate(self.banco_de_dados.lista_veiculos()):
            print(f'Veículo {i + 1}:')
            veiculo.print_veiculo()
            print()
    