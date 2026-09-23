#5. Find the factorial of a number

n = int(input("Enter any number to find factorial:"))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial:", fact)
