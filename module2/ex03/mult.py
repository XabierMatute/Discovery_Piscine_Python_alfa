print("Enter the first number:")
n1 = int(input())
print("Enter the second number:")
n2 = int(input())
number = n1 * n2
print(f"{n1} x {n2} = {number}")
if number == 0:
    print("This number is both positive and negative.")
if number > 0:
    print("This number is positive.")
if number < 0:
    print("This number is negative.")


