
from datetime import date

class User:
    def __init__(self, name: str, date_of_birth: date):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self) -> int:
        today = date.today()
        years = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years


def require_adult(func):
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        for arg in all_args:
            if isinstance(arg, User):
                if arg.age < 18:
                    raise PermissionError(f"User {arg.name} is under 18!")
        return func(*args, **kwargs)
    return wrapper


@require_adult
def register_account(user: User):
    return f"Account created for {user.name}, age {user.age}"


Robinson = User("Robinson", date(1992, 11, 3)) 
Tabata = User("Tabata", date(2010, 7, 15))      

print(register_account(Robinson))  
print("-----NEXT ONE IS UNDER AGE!!-----")
print(register_account(Tabata))     
