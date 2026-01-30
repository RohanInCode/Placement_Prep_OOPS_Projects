class Employee:
    def __init__(self,name,emp_id):
        self.emp_id=emp_id
        self.name=name
    def calculate_salary(self):
        pass

class FulltimeEmployee(Employee):
    def __init__(self,emp_id,name,monthly_salary):
        super().__init__(emp_id,name)
        self._monthly_salary=monthly_salary
        #Encapsulation because salary is protected
    def calculate_salary(self):
        return self._monthly_salary
class ParttimeEmployee(Employee):
    def __init__(self, name, emp_id,hours_worked,rate_per_hour):
        super().__init__(name, emp_id)
        self._hours_worked = hours_worked
        self._rate_per_hour=rate_per_hour
    def calculate_salary(self):
        return self._hours_worked * self._rate_per_hour

class PayrollApp:
    def __init__(self):
        self.employee=None
    def create_employee(self,emp_type):
        if emp_type=="Fulltime":
            self.employee=FulltimeEmployee("Rohan",1,10000)
        else:
            self.employee=ParttimeEmployee("Abhishek",2,45,200)
        return "Employee Created"
    
    def get_salary(self):
        return self.employee.calculate_salary()

app = PayrollApp()

print(app.create_employee("Fulltime"))
print("Salary:", app.get_salary())

print()

print(app.create_employee("Parttime"))
print("Salary:", app.get_salary())
