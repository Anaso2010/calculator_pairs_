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
            elif operation == "Multiply":
                result = a * b
            elif operation == "Divide":
                if b == 0:
                    result_basic.value = "Error: Divide by zero"
                    page.update()
                    return
                result = a / b

            result_basic.value = f"Result: {result}"

        except ValueError:
            result_basic.value = "Error: Invalid input"

        page.update()

    basic_tab = ft.Column([
        ft.Row([num1, num2]),
        ft.Row([
            ft.ElevatedButton("Add", on_click=calculate_basic),
            ft.ElevatedButton("Subtract", on_click=calculate_basic),
            ft.ElevatedButton("Multiply", on_click=calculate_basic),
            ft.ElevatedButton("Divide", on_click=calculate_basic),
        ]),
        result_basic
    ])

    page.add(basic_tab)

ft.app(target=main)