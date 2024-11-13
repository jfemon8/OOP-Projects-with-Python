from menu import Menu

class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()
    
    def add_employee(self, employe):
        self.employees.append(employe)
        
    def view_employee(self):
        print("** Employee List **")
        print("  Name |  Email Address  |  Phone  |  Address  |  Age  |  Designation  |  Salary  ")
        for emp in self.employees:
            print(f'{emp.name}  |  {emp.email}  |  {emp.phone}  |  {emp.address}  |  {emp.age}  |  {emp.designation}  |  {emp.salary}')

