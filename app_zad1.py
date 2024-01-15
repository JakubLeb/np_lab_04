def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b

def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Dzielenie przez zero jest niedozwolone.")
    return a / b

if __name__ == "__main__":
    num1 = 20
    num2 = 8
    print(f"Dodawanie: {add_numbers(num1, num2)}")
    print(f"Odejmowanie: {subtract_numbers(num1, num2)}")
    print(f"Mnożenie: {multiply_numbers(num1, num2)}")
    print(f"Dzielenie: {divide_numbers(num1, num2)}")
