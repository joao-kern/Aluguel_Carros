from sistema.repositorios.banco_de_dados import BancoDados
from sistema.sistema import Sistema
from sistema.modelos.administrador import Adm

def main():
    banco_de_dados = BancoDados()
    banco_de_dados.adicionar_cliente('João', 99345423234, '48991881406', 'joaovictorramoskern@gmail.com', 81641633912, '0lgT5UY16Lnh')
    banco_de_dados.adicionar_cliente('Pedro', 99345420718, '4899187636', 'pedroroberto123@gmail.com', 51162930520, 'RKXcTic6hE')
    banco_de_dados.adicionar_cliente('Luisa', 99345423234, '48997564323', 'luisasilva@gmail.com', 87736587301, 'b2m1cpfmMY5F')
    banco_de_dados.adicionar_veiculos('MWK7949', 'Ferrari', 'F-90', 2019, 800)
    banco_de_dados.adicionar_veiculos('DXI4781', 'Lotus', 'F-Elan', 1995, 200)
    banco_de_dados.adicionar_veiculos('MZD5060', 'Porsche', '911 GT3 RS', 2022, 650)

    adm = Adm()
    sistema = Sistema(banco_de_dados, adm)

    sistema.executar()

if __name__ == '__main__':
    main()
