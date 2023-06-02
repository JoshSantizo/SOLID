from abc import ABC
from datetime import date
from employee import Employee


class Report(ABC):
    def __init__(self, name: str):
        self.name = name
        self.entry = date.today()
        self.employees: list[Employee] = []

    def generate_report(self):
        raise NotImplementedError

    def add_employee(self, employee: Employee):
        raise NotImplementedError
