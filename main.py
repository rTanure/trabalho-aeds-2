import csv
import os

from controllers.employee import *
from controllers.markTime import *

def create_data_files():
  files = [
    (EMPLOYEE_DATA_PATH, EMPLOYEE_DATA_HEADERS),
    (MARK_TIME_DATA_PATH, MARK_TIME_DATA_HEADERS)
  ]



  for path, header in files:
    if(not os.path.exists(path)):
      with open(path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header);

if __name__ == "__main__":
  create_data_files()

  add_new_employee("Carlos", 8, 18)

  employee = get_employee_by_id(29543)
  print(employee)

  update_employee_state(29543, "inside")