class FinanceManager:

    def __init__(self):
        self.categories = []
        self.movements = []

    def add_category(self, name):
        if name not in self.categories:
            self.categories.append(name)

    def add_movement(self, movement):
        self.movements.append(movement)
