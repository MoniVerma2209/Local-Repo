#Calculator
a = float(input("Enter First Number:"))
b = float(input("Enter Second Number:"))
op = input("Add Operator (+, -, *, **, /, %):")

if op == '+':
    print(a + b)
elif op == '-':   
    print(a - b)
elif op == '*':   
    print(a * b)
elif op == '**':   
    print(a ** b)
elif op == '/':   
    print(a / b)
elif op == '%':   
    print(a % b)
else:
    print("Invalid Operation")    



