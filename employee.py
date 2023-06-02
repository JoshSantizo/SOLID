from faker import Faker
from attendance import Attendence
fake = Faker()


class Employee:
    def __init__(self):
        self.__name = fake.name()
        self.__lastname = fake.last_name()
        self.__role = fake.job()
        self.__attendances: list[Attendence] = []
        self.__attendances.append(Attendence(fake.date_time()))
        self.__attendances.append(Attendence(fake.date_time()))

    def get_name(self):
        return f'{self.__name}, {self.__lastname}'

    def get_attendance(self):
        return self.__attendances
