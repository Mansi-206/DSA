#7. Create a simple calculator using if-elif-else

a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
operator = input("Enter any oprator:")

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    print("Result:", a / b)
else:
    print("Invalid operator")
