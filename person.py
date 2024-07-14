class Person:
    def __init__(self, name: str, cpf: str, rg: str, birth: str):
        self.birth = birth
        self.name = name
        self.cpf = cpf
        self.rg = rg

    @property
    def birth(self):
        return self.name

    @birth.setter
    def birth(self, birth: str):
        self.__birth: str = birth

    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def name(self, name):
        self.__name: str = name

    @property
    def cpf(self) -> str:
        return self.cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf: str = cpf

    @property
    def rg(self) -> str:
        return self.rg

    @rg.setter
    def rg(self, rg):
        self.__rg: str = rg

    def show_information(self):
        print(f'Name: {self.name}')
        print(f'CPF: {self.cpf}')
        print(f'RG: {self.rg}')
        print(f'Birth: {self.birth}')
