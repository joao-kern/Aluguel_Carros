from cliente import Cliente
from aluguel import Aluguel
from veiculo import Veiculo

class BancoDados:
    def __init__(self):
        self._clientes = []
        self._veiculos = []
        self._alugueis = []
        self._renda_dia = 0
    
    def lista_clientes(self):
        return self._clientes
    
    def adicionar_cliente(self, nome, cpf, telefone, email, cnh, senha):
        cliente = Cliente(nome, cpf, telefone, email, cnh, senha)
        self._clientes.append(cliente)

    def buscar_cliente(self, cpf):
        for cliente in self._clientes:
            if cliente.cpf == cpf:
                return cliente
    
        return None        
    
    def lista_veiculos(self):
        return self._veiculos
    
    def adicionar_veiculos(self, placa, marca, modelo, ano, valor_diaria):
        veiculo = Veiculo(placa, marca, modelo, ano, valor_diaria)     
        self._veiculos.append(veiculo)

    def buscar_veiculo(self, placa):
        for veiculo in self._veiculos:
            if veiculo.placa == placa:
                return veiculo
            
        return None

    def verifica_status_veiculo(self, veiculo):
        if veiculo.status == 'Disponível':
            return True
        else:
            return False
        
    def remover_veiculo(self, placa):
        removido = False
        for veiculos in self._veiculos:
            if veiculos.placa == placa:
                veiculo = veiculos
                self._veiculos.remove(veiculo)
                del(veiculo)
                removido = True
                return removido
        return removido   

    def lista_alugueis(self):
        return self._alugueis

    def adicionar_alugueis(self, data_inicio, data_termino, cliente, veiculo):
        aluguel = Aluguel(data_inicio, data_termino, cliente, veiculo)
        valor_aluguel = aluguel.valor_aluguel()
        self._renda_dia += valor_aluguel
        self._alugueis.append(aluguel)
        return aluguel
    
    def buscar_aluguel(self, cliente, veiculo):
        for alugueis in self._alugueis:
            if alugueis.cliente == cliente and alugueis.veiculo == veiculo:
                aluguel = alugueis
                return aluguel

        return None

    def buscar_alugueis_cliente(self, cliente):
        alugueis_cliente = []
        for alugueis in self._alugueis:
            if alugueis.cliente == cliente:
                alugueis_cliente.append(alugueis)

        return alugueis_cliente

    def receita(self):
        return self._renda_dia

    def alterar_renda_diaria(self, valor):
        self._renda_dia += valor

    def finalizar_dia(self):
        self._alugueis = []
        self._renda_dia = 0



    