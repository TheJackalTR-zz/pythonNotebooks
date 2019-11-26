print("""**************************
Calculator Application

Operations;

1. Summation

2. Subtraction

3. Multiplication

4. Division
**************************
""")

a = int(input("First number: "))
b = int(input("Second number: "))

operation = input("Enter the operation: ")

if operation == "1":
    print("Summation of {} and {} is {}".format(a, b, a + b))
elif operation == "2":
    print("Subtraction of {} and {} is {}".format(a, b, a - b))
elif operation == "3":
    print("Multiplication of {} and {} is {}".format(a, b, a * b))
elif operation == "4":
    print("Division of {} and {} is {}".format(a, b, a / b))
else:
    print("There isn't any operation like that")
