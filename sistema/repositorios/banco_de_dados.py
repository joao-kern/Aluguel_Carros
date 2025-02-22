from typing import List
from sistema.modelos.cliente import Cliente
from sistema.modelos.aluguel import Aluguel
from sistema.modelos.veiculo import Veiculo

class BancoDados:
    def __init__(self) -> None:
        self._clientes: List[Cliente] = []
        self._veiculos: List[Veiculo] = []
        self._alugueis: List[Aluguel] = []
        self._renda_dia:float = 0
    
    def lista_clientes(self):
        return self._clientes
    
    def adicionar_cliente(self, nome, cpf, telefone, email, cnh, senha) -> None:
        cliente = Cliente(nome, cpf, telefone, email, cnh, senha)
        self._clientes.append(cliente)

    def buscar_cliente(self, cpf) -> Cliente | None:
        for cliente in self._clientes:
            if cliente.cpf == cpf:
                return cliente
    
        return None        
    
    def lista_veiculos(self) -> List[Veiculo]:
        return self._veiculos
    
    def adicionar_veiculos(self, placa, marca, modelo, ano, valor_diaria) -> None:
        veiculo = Veiculo(placa, marca, modelo, ano, valor_diaria)     
        self._veiculos.append(veiculo)

    def buscar_veiculo(self, placa) -> Veiculo | None:
        for veiculo in self._veiculos:
            if veiculo.placa == placa:
                return veiculo
            
        return None

    def verifica_status_veiculo(self, veiculo) -> bool:
        if veiculo.status == 'Disponível':
            return True
        else:
            return False
        
    def remover_veiculo(self, placa) -> bool:
        removido = False
        for veiculos in self._veiculos:
            if veiculos.placa == placa:
                veiculo = veiculos
                self._veiculos.remove(veiculo)
                del(veiculo)
                removido = True
                return removido
        return removido   

    def lista_alugueis(self) -> List[Aluguel]:
        return self._alugueis

    def adicionar_alugueis(self, data_inicio, data_termino, cliente, veiculo) -> Aluguel:
        aluguel = Aluguel(data_inicio, data_termino, cliente, veiculo)
        valor_aluguel = aluguel.valor_aluguel()
        self._renda_dia += valor_aluguel
        self._alugueis.append(aluguel)
        return aluguel
    
    def buscar_aluguel(self, cliente, veiculo) -> Aluguel | None:
        for alugueis in self._alugueis:
            if alugueis.cliente == cliente and alugueis.veiculo == veiculo:
                aluguel = alugueis
                return aluguel

        return None

    def buscar_alugueis_cliente(self, cliente) -> List[Aluguel]:
        alugueis_cliente = []
        for alugueis in self._alugueis:
            if alugueis.cliente == cliente:
                alugueis_cliente.append(alugueis)

        return alugueis_cliente

    def receita(self) -> float:
        return self._renda_dia

    def alterar_renda_diaria(self, valor) -> None:
        self._renda_dia += valor

    def finalizar_dia(self) -> None:
        self._alugueis = []
        self._renda_dia = 0



    