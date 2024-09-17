def add_everything_up(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, float) and isinstance(b, float):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        return f"{a}{b}"
    
print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))