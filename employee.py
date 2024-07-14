from person import Person


class Employee(Person):
    def __init__(self, id_employee: int, position: str, name: str, cpf: str, rg: str, birth: str) -> None:
        super().__init__(name, cpf, rg, birth)
        self.id_employee = id_employee
        self.position = position

    @property
    def id_employee(self) -> int:
        return self.__id_employee

    @property
    def position(self) -> str:
        return self.__position

    @id_employee.setter
    def id_employee(self, id_employee: int):
        self.__id_employee: int = id_employee

    @position.setter
    def position(self, position: str) -> None:
        self.__position: str = position

    def show_information(self) -> None:
        super().show_information()
        print(f"Id: {self.id_employee}")
        print(f"Position: {self.position}")

    def calculating_overtime(self):
        ...

    def get_company_time(self):
        ...
