from employee import Employee
from typing import List
from input import read_input_data_mark_time
import tools


# Mark point, check if there is already a file with the name, if there is writing to it, if not create and
# write
def mark_point(employee: Employee) -> bool:
    name_file = employee.name + '_' + str(employee.id_employee)
    file_existent: bool = tools.verify_existent_file(name_file)
    if file_existent:
        with open(f'{name_file}.dat', 'a') as file:
            file.write(f'Name employee: {employee.name}, ')
            file.write(f'Id employee: {employee.id_employee}, ')
    else:
        with open(f'{name_file}.dat', 'w') as file:
            file.write(f'Name employee: {employee.name}, ')
            file.write(f'Id employee {employee.id_employee}, ')
    return True


class Company:
    def __init__(self, name: str, cpj: str, name_fantasy: str):
        self.name: str = name
        self.cpj: str = cpj
        self.name_fantasy: str = name_fantasy
        self.__employees: List[Employee] = []

    @property
    def name(self) -> str:
        return self.__name

    @property
    def cpj(self) -> str:
        return self.__cpj

    @property
    def name_fantasy(self) -> str:
        return self.__name_fantasy

    @name.setter
    def name(self, name) -> None:
        self.__name: str = name

    @cpj.setter
    def cpj(self, cpj) -> None:
        self.__cpj: str = cpj

    @name_fantasy.setter
    def name_fantasy(self, name_fantasy) -> None:
        self.__name_fantasy: str = name_fantasy

    def register_employee(self, id_employee, position, name, cpf, rg, birth) -> None:
        self.__employees.append(Employee(id_employee, position, name, cpf, rg, birth))

    def get_list_employees(self) -> [Employee]:
        return self.__employees

    def get_employee_by_id(self, id_employee) -> Employee:
        for employee in self.__employees:
            if employee.id_employee == id_employee:
                return employee

        return None
