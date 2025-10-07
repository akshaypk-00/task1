# task 3

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class Manager(Employee):
    def calculate_salary(self):
        return self.salary + 2000

class Developer(Employee):
    def calculate_salary(self):
        return self.salary + 1000

class Intern(Employee):
    def calculate_salary(self):
        return self.salary - 500

m = Manager("Hari", 15000)
d = Developer("Abhi", 14000)
i = Intern("Adi", 20000)

print("Monthly Salaries:")
print(m.name, "=", m.calculate_salary())
print(d.name, "=", d.calculate_salary())
print(i.name, "=", i.calculate_salary())
