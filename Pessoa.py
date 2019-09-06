class Pessoa:
    def __init__(self, atributos):  # adicionar 15 atributos a partir dos dados da PNAD de 2014
        if atributos[0] == 0:  # redimento domiciliar
            self.rend_dom = 'Entre 0 e 1 salários mínimos'
        elif atributos[0] == 1:
            self.rend_dom = 'Entre 1 e 2 salários mínimos'
        elif atributos[0] == 2:
            self.rend_dom = 'Entre 2 e 3 salários mínimos'
        elif atributos[0] == 3:
            self.rend_dom = 'Entre 3 e 5 salários mínimos'
        elif atributos[0] == 4:
            self.rend_dom = 'Entre 5 e 10 salários mínimos'
        elif atributos[0] == 5:
            self.rend_dom = 'Entre 10 e 20 salários mínimos'
        elif atributos[0] == 6:
            self.rend_dom = 'Mais de 20 salários mínimos'
        elif atributos[0] == 7:
            self.rend_dom = 'Sem declaração'

        if atributos[1] == 0:  # rede de ensino
            self.rede = 'Pública'
        elif atributos[1] == 1:
            self.rede = 'Particular'

        if atributos[2] == 0:  # modalidade
            self.mod = 'Presencial'
        elif atributos[2] == 1:
            self.mod = 'À distância'

        if atributos[3] == 0:  # sexo
            self.sexo = 'Homem'
        elif atributos[3] == 1:
            self.sexo = 'Mulher'

        if atributos[4] == 0:  # cor ou raça
            self.cor = 'Branca'
        elif atributos[4] == 1:
            self.cor = 'Preta ou parda'
