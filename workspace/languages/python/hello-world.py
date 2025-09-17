def add(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b

def mul(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int) -> float:
    if  b == 0:
        raise ZeroDivisionError("Divide by zero error, b should be non zero")
    return a / b


a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))

print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {sub(a, b)}")
print(f"{a} * {b} = {mul(a, b)}")

try:
    print(f"{a} / {b} = {div(a, b)}")
except ZeroDivisionError as e:
    print(f"{a} / {b}", e)
