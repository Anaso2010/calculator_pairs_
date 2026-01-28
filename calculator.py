import flet as ft
 
def main(page: ft.Page):
 
    num1 = ft.TextField(label="Number 1", width=150)
    num2 = ft.TextField(label="Number 2", width=150)
    result_basic = ft.Text("Result:")
 
    def calculate_basic(e):
        try:
            a = float(num1.value)
            b = float(num2.value)
            operation = e.control.text
 
            if operation == "Add":
                result = a + b
            elif operation == "Subtract":
                result = a - b
 
        except ValueError:
            result_basic.value = "Error: Invalid input"

ft.app(main)