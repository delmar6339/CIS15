class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name, salary)

    def calculate_long_term_bonus(self):
        return self.salary * 0.4
      
manager = Manager("Konnor", "Del Mar", 90000000)
print(f"Manager: {manager.get_full_name()}")
print(f"Salary: ${manager.get_salary():,.2f}")
print(f"Long-term Bonus: ${manager.calculate_long_term_bonus():,.2f}")