from report import Report
from reportlab.pdfgen import canvas
from employee import Employee


class PDFReport(Report):
    def __init__(self, name: str):
        super().__init__(name)

    def generate_report(self):
        y: int = 750
        pdf = canvas.Canvas(self.name)
        for employee in self.employees:
            pdf.drawString(100, y, f'NOMBRE: {employee.get_name()}')
            for fecha in employee.get_attendance():
                pdf.drawString(100, y - 20, f'- ASISTENCIA: {fecha.current_date} - {fecha.is_on_time()}')
                y -= 20
            y -= 60

        pdf.save()

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
