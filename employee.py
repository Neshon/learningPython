class Employee:
    """Класс описывает работника"""
    def __init__(self, first_name, last_name, salary):
        """Сохраняет имя, фамилию, зарплату"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, salary_increase=5000):
        """Прибавка к зарплате. По умолчания 5000"""
        self.salary += salary_increase
        return self.salary

