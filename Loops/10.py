#10. Print Fibonacci series up to n terms

n = int(input("Enter number:"))

a = 0
b = 1

for i in range(n):
    print(a)
    a, b = b, a + b
