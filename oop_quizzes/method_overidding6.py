class Employee:
    def calculate_salary(self):
        print("Calculating generic employee salary")

class Manager(Employee):
    def calculate_salary(self):
        print("Calculating manager's salary")

# Demonstration
emp = Employee()
mgr = Manager()
emp.calculate_salary()  # Outputs: Calculating generic employee salary
mgr.calculate_salary()  # Outputs: Calculating manager's salary
