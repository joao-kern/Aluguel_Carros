from datetime import datetime

from sistema.modelos.cliente import Cliente
from sistema.modelos.veiculo import Veiculo

class Aluguel:
    def __init__(self, data_inicio, data_termino, cliente, veiculo) -> None:
        self.data_inicio: datetime = data_inicio
        self.data_termino: datetime = data_termino
        self.devolucao_realizada: str = 'Não'
        self.cliente: Cliente = cliente
        self.veiculo: Veiculo = veiculo
        self.danos: str = 'Não'
        self.valor: float = 0
        self.dias_atrasados: int = 0
        self.multa: float = 0

    def verifica_multa(self, data_devolucao, danos) -> float:
        taxa_diaria_multa = 100
        taxa_danos = 250
        self.dias_atrasados = (data_devolucao - self.data_termino).days
        if  self.dias_atrasados > 0:
            self.multa += taxa_diaria_multa * self.dias_atrasados

        if danos == 'S':
            self.danos = 'Sim'
            self.multa += taxa_danos
        
        return self.multa

    def confirmar_devolucao(self, data_devolucao) -> None:
        self.devolucao_realizada = data_devolucao

    def valor_aluguel(self) -> float:
        dias = (self.data_termino - self.data_inicio).days
        valor_aluguel = dias * self.veiculo.valor_diaria
        return valor_aluguel
    
    def print_aluguel(self) -> None:
        print(f'Placa Veiculo: {self.veiculo.placa}')
        print(f'Modelo Veículo: {self.veiculo.modelo}')
        print(f'Data de início: {self.data_inicio}')
        print(f'Data de fim: {self.data_termino}')
        print(f'Devolução realizada: {self.devolucao_realizada}')
        print(f'Valor: R$ {self.valor_aluguel()}')
        print(f'Dias atrasados: {self.dias_atrasados}')
        print(f'Multa: R$ {self.multa}')
        print()
        