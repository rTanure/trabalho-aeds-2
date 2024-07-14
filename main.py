#import sys
#import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), './../employee')))
import company
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), './../input_module')))
#from input import ready_input_user


company_1 = company.Company('coursera', 000000, 'company')

company_1.register_employee(111, 'aaaa', 'pedro', 111, '111', '23/04/2004')
