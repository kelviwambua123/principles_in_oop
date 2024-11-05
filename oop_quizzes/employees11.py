class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_payroll(self):
        total = sum(employee.salary for employee in self.employees)
        print("Total Payroll:", total)
        return total

# Demonstration
emp1 = Employee("Alice", 5000)
emp2 = Employee("Bob", 7000)
payroll = Payroll()
payroll.add_employee(emp1)
payroll.add_employee(emp2)
payroll.calculate_total_payroll()  # Outputs the total payroll
