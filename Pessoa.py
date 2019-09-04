class Pessoa:
    def __init__(self, atributos):  # adicionar 15 atributos a partir dos dados da PNAD de 2014
        self.rend_dom = atributos[0]  # redimento domiciliar
        self.rede = atributos[1]  # rede de ensino
        self.mod = atributos[2]  # modalidade
        self.sexo = atributos[3]  # sexo
        self.cor = atributos[4]  # cor ou raça

