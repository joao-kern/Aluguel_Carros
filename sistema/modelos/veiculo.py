class Veiculo:
    def __init__(self, placa: str, marca: str, modelo: str, ano: int, valor_diaria: float):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
        self.status: str = 'Disponível'
        self._quilometragem: float = 0

    def alterar_status(self, status):
        self.status = status

    def valor_status(self):
        return self.status
    
    def alterar_quilometragem(self, quilometragem_andada):
        self._quilometragem += quilometragem_andada

    def valor_quilometragem(self):
        return self._quilometragem
    
    def print_veiculo(self):
        print(f'Veículo')
        print(f'Placa: {self.placa}')
        print(f'Modelo: {self.modelo}')
        print(f'Marca: {self.marca}')
        print(f'Ano: {self.ano}')
        print(f'Status: {self.status}')
        print(f'Valor Diária: R$ {self.valor_diaria}')
        print(f'Quilometragem: {self.valor_quilometragem()}')
        print()