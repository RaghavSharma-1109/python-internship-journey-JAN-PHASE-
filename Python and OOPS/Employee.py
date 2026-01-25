class Employee:
    increement = 1.06
    def __init__(self,name,salary):
        self.Name = name
        self.Salary = salary
    def annual_salary(self):
        return self.Salary
    def is_high_earner(self):
        return self.annual_salary()>1000000
    def apply_raise(self):
        self.Salary *= self.increement
        return self.Salary

emp_1 = Employee('Raghav', 24500000)

print(emp_1.annual_salary())
print(emp_1.is_high_earner())
print(emp_1.apply_raise())


