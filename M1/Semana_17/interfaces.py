import FreeSimpleGUI as sg

class Interfaces:

    def __init__(self, window_type):
        self.window_type = window_type

    def create_window(self, categories):

        if self.window_type == "category":
            layout = [
                [sg.Text("Enter the new category data")],
                [
                    sg.Text(self.window_type),
                    sg.Input(size=10, key="categoryName"),
                    sg.Button("Confirm " + self.window_type)
                ]
            ]
            return sg.Window(self.window_type, layout, finalize=True)

        layout = [
            [sg.Text(self.window_type)],
            [sg.Text("Description"), sg.Input(size=10, key="description")],
            [sg.Text("Amount"), sg.Input(size=10, key="amount")],
            [
                sg.Text("Category"),
                sg.Combo(
                    categories,
                    default_value="Open to see more options",
                    enable_events=True,
                    key="comboCategories"
                )
            ],
            [sg.Button("Confirm " + self.window_type)]
        ]

        return sg.Window(self.window_type, layout, finalize=True)
