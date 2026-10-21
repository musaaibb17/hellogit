print("===== Simple Calculator =====")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

num1 = float(input("Enter first number: "))
operator = input("?enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2  
    else:
        result = " Error: Cannot divide by zero"
else:
    result = "Invalid operator"
print("Result:", result)                         