class Head:
    pass


class Hand:
    pass


class Arm:
    def __init__(self, hand: Hand):
        self.hand = hand


class Feet:
    pass


class Leg:
    def __init__(self, foot: Feet):
        self.foot = foot


class Torso:
    def __init__(self, head: Head, left_arm: Arm, right_arm: Arm, left_leg: Leg, right_leg: Leg):
        self.head = head
        self.left_arm = left_arm
        self.right_arm = right_arm
        self.left_leg = left_leg
        self.right_leg = right_leg


class Human:
    def __init__(self):
        # Creamos cada parte del cuerpo
        head = Head()

        left_hand = Hand()
        right_hand = Hand()

        left_arm = Arm(left_hand)
        right_arm = Arm(right_hand)

        left_foot = Feet()
        right_foot = Feet()

        left_leg = Leg(left_foot)
        right_leg = Leg(right_foot)

        # El torso une todo
        self.torso = Torso(head, left_arm, right_arm, left_leg, right_leg)

    def describe(self):
        print("This human has:")
        print("- 1 head")
        print("- 2 arms (each with a hand)")
        print("- 2 legs (each with a foot)")


person = Human()
person.describe()
