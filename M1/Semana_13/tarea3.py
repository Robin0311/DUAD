def ensure_numbers(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError(f"Argument {arg} is not a number")
        
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(f"Argument '{key}={value}' is not a number")
        
        return func(*args, **kwargs)
    return wrapper


@ensure_numbers
def add(a, b):
    return a + b

print(add(3, 5))        
print(add(a=2, b=4.5))  
#print(add(3, "hello"))  # tira error