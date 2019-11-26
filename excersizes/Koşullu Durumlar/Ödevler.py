# %% BMI -

height = float(input("Enter your height(Example:1.77):"))
weight = float(input("Enter your weight:"))

BMI = weight / (height * height)

if BMI < 18.5:
    print("You are thin")
elif 18.5 <= BMI < 25:
    print("You are in normal weight")
elif 25 <= BMI < 30:
    print("You are overweight")
else:
    print("You are obese")

# %%  Take 3 number from user and find the highest

a = int(input("Enter first number: "))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

if a > b and a > c:
    print("The highest number is: ", a)
elif b > a and b > c:
    print("The highest number is: ", b)
else:
    print("The highest number is: ", c)

# %% midterm1, midterm2 and final note's Grade Midterm1 will be effect %30, midterm2 will be affect %30
# Final will be effect %40 or grade

midterm1 = int(input("Enter your midterm 1 exam grade:"))
midterm2 = int(input("Enter your midterm 2 exam grade:"))
final = int(input("Enter your final exam grade:"))

letterGrade = midterm1 * 0.30 + midterm2 * 0.30 + final * 0.40

print(letterGrade)

if 100 >= letterGrade >= 90:
    print("Your letter grade is AA")
elif 90 > letterGrade >= 85:
    print("Your letter grade is BA")
elif 85 > letterGrade >= 80:
    print("Your letter grade is BB")
elif 80 > letterGrade >= 75:
    print("Your letter grade is CB")
elif 75 > letterGrade >= 70:
    print("Your letter grade is CC")
elif 70 > letterGrade >= 65:
    print("Your letter grade is DC")
elif 65 > letterGrade >= 60:
    print("Your letter grade is DD")
elif 60 > letterGrade >= 55:
    print("Your letter grade is FD")
elif 55 > letterGrade:
    print("Your letter grade is FF")
else:
    print("Unrecognizable Grade")

# %%
print("""********************
you can choose from 

1. Triangle

2. Quadrilateral
********************
""")

operation = int(input("Enter an operation:"))

if operation == 1:
    x = float(input("Enter first side of triangle:"))
    y = float(input("Enter the second side of triangle:"))
    z = float(input("Enter the third side of triangle:"))
    if abs(y - z) < x < (y + z) and \
            abs(x - z) < y < x + z and \
            abs(x - y) < z < x + y:
        print("That's a Triangle")
        if x == y == z:
            print("That's an equilateral triangle")
        elif x == y or y == z or x == z:
            print("That's an isosceles triangle")
        else:
            print("That's a scalar triangle")
    else:
        print("That's not a Triangle")

elif operation == 2:
    a = float(input('Enter the first side of Quadrilateral'))
    b = float(input('Enter the second side of Quadrilateral'))
    c = float(input('Enter the third side of Quadrilateral'))
    d = float(input('Enter the fourth side of Quadrilateral'))
    if a == b == c == d:
        print("It's a square")
    elif a == b and c == d or a == c and b == d or a == d and b == c:
        print("It's a rectangle")
    else:
        print("It's an ordinary rectangle")
else:
    print("Unrecognizable operation, please try again")
