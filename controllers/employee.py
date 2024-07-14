# Funções de manipulação de usuários
# criar, deletar, editar, perquisar, listar
import csv
import random

EMPLOYEE_DATA_HEADERS = [
  "id",
  "name",
  "start_of_shift",
  "end_of_shift",
  "state" # inside | outside
]

EMPLOYEE_DATA_PATH = "data/employee.csv"

def add_new_employee(name, start_of_shift, end_of_shift):
  with open(EMPLOYEE_DATA_PATH, "a") as file:

    # Cria um id único
    id = None
    is_unique_id = False
    while(not is_unique_id):
      id = random.randint(10000, 99999)
      employee = get_employee_by_id(id)
      if employee is None:
        is_unique_id = True

    # Define o estado inicial do funcionário
    state = "outside"

    # Escreve no arquivo
    file.write(f"{id},{name},{start_of_shift},{end_of_shift},{state}\n")

def get_employee_by_id(id: int):
  with open(EMPLOYEE_DATA_PATH, "r") as file:
    reader = csv.reader(file)

    for row in reader:
      if row[0] != "id": # Pular o header do CSV
        if int(row[0]) == id: # Verifica se o ID é o passado
          employee = {
            "id": row[0],
            "name": row[1],
            "start_of_shift": row[2],
            "end_of_shift": row[3],
            "state": row[4]
          }
          return employee
  return None

# Implementar forma que não carrega dados na memoria
def update_employee_state(id, state):
  if(state not in ["inside", "outside"]): return False
  if(get_employee_by_id(id) is None): return False
  
  with open(EMPLOYEE_DATA_PATH, "r") as file:
    data = list(csv.reader(file))

  row_index = None
  for i, row in enumerate(data):
    if row[0] == str(id):
      row_index = i
      break

  if row_index is not None:
    data[row_index][4] = state
    with open(EMPLOYEE_DATA_PATH, "w", newline="") as file:
      writer = csv.writer(file)
      writer.writerows(data)

      return True

  return False
