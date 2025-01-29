def greet():
    print("Hello, Welcome to Python!")

greet()  
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)
def power(base, exp=2):
    return base ** exp
print("Power:", power(3))  
print("Power:", power(3, 3))  
def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
print("Multiplication:", multiply(2, 3, 4))
def display_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
display_info(name="Alice", age=25, city="New York")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))
