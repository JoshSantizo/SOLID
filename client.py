from employee import Employee
from pdf_report import PDFReport
from xls_report import XLSReport


class Client:
    def __init__(self):
        self.__employees: list[Employee] = []
        self.__employees = [Employee(), Employee(), Employee()]

    @staticmethod
    def menu():
        print('1. Reporte PDF')
        print('2. Reporte EXCEL')
        print('3. Terminal')
        print('4. Agregar empleado')
        print('5. Salir')

    def main_menu(self):
        option: int = 0
        while option != 5:
            self.menu()
            option = int(input('Selecciona una opccion: '))
            if option == 1:
                self.pdf_report()
            elif option == 2:
                self.xlsx_report()
            elif option == 3:
                self.terminal()
            elif option == 4:
                self.__employees.append(Employee())

    def pdf_report(self):
        pdf = PDFReport("Reporte.pdf")
        for employee in self.__employees:
            pdf.add_employee(employee)
        pdf.generate_report()

    def xlsx_report(self):
        xls = XLSReport("Reporte.xlsx")
        for employee in self.__employees:
            xls.add_employee(employee)
        xls.generate_report()

    def terminal(self):
        for employee in self.__employees:
            print(f'Nombre: {employee.get_name()}')
            print('-Asistencia: ')
            for fecha in employee.get_attendance():
                print(f'{fecha.current_date} | {fecha.is_on_time()}')
