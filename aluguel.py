class Aluguel:
    def __init__(self, data_inicio, data_termino, cliente, veiculo):
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.devolucao_realizada = 'Não'
        self.cliente = cliente
        self.veiculo = veiculo
        self.danos = 'Não'
        self.valor = 0
        self.dias_atrasados = 0
        self.multa = 0

    def verifica_multa(self, data_devolucao, danos):
        taxa_diaria_multa = 100
        taxa_danos = 250
        self.dias_atrasados = (data_devolucao - self.data_termino).days
        if  self.dias_atrasados > 0:
            self.multa += taxa_diaria_multa * self.dias_atrasados

        if danos == 'S':
            self.danos = 'Sim'
            self.multa += taxa_danos
        
        return self.multa

    def confirmar_devolucao(self):
        self.devolucao_realizada = 'Sim'

    def valor_aluguel(self):
        dias = (self.data_termino - self.data_inicio).days
        valor_aluguel = dias * self.veiculo.valor_diaria
        return valor_aluguel
    
    def print_aluguel(self):
        print(f'Placa Veiculo: {self.veiculo.placa}')
        print(f'Modelo Veículo: {self.veiculo.modelo}')
        print(f'Data de início: {self.data_inicio}')
        print(f'Data de fim: {self.data_termino}')
        print(f'Devolução realizada: {self.devolucao_realizada}')
        print(f'Valor: R$ {self.valor_aluguel()}')
        print(f'Dias atrasados: {self.dias_atrasados}')
        print(f'Multa: R$ {self.multa}')
        print()
        