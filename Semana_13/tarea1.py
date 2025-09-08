def count_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} has been called {count} times")
        return func(*args, **kwargs)
    return wrapper


@count_calls
def greet(name):
    return f"Hello, {name}!"

print(greet("Robinson"))
print(greet("Bryan"))

