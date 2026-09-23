#3. Find the largest of three numbers

a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
c = int(input("Enter value of c:")) 

if a > b and a > c:
    print("Largest:", a)
elif b > a and b > c:
    print("Largest:", b)
else:
    print("Largest:", c)
