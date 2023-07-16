# Aggregation - Example


# class salary
class Salary:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def yearly_salary(self):
        return (self.base * 12) + self.bonus


# class employee
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.earned_salary = salary  # Aggregation

    def total_salary(self):
        return print(f"{self.name} Your total salary is: {self.earned_salary.yearly_salary()}")


salary = Salary(1000, 700)
emp = Employee("John", 35, salary)
print(emp.total_salary())
