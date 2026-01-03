class Logic:

    def __init__(self, movement_type, description, amount, category):
        self.movement_type = movement_type
        self.description = description
        self.amount = amount
        self.category = category

    def create_movement(self):
        if self.movement_type == "Income":
            return [self.movement_type, self.description, self.amount, self.category]

        return [self.movement_type, self.description, -self.amount, self.category]
