def print_params_functions(func):
    def wrapper(*args, **kwargs):
        if args:
            print(f"args: {args}")
        if kwargs:
            print(f"kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result

    return wrapper

@print_params_functions
def sum_params(a, b):
    return a + b

@print_params_functions
def introduction(age, name):
    return f"Hi my name is {name} and im {age} years old"


sum_params(5, 3)
introduction(32, name="Robinson")
