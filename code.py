#Calculator
a = float(input("Enter First Number:"))
b = float(input("Enter Second Number:"))
op = input("Enetr operator (+, -, *, **, /, %,):")
if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)    
if op == '*':
    print(a * b)
elif op == '**':
    print(a ** b)
if op == '/':
    print(a / b)
elif op == '%':
    print(a % b)    
else:
    print("Invalid Operator")






