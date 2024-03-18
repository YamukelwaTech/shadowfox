# Task 1
# function with erro handiling


def representation(num, char):
    # Check if num is a valid integer
    if not isinstance(num, int):
        return "Invalid input for num: '{}' is not an integer".format(num)
    string = "Number: {:d}, letter: '{}'".format(num, char)
    return string


answers = representation(45, "o")
print(answers)


# Task 2


def area(radius, pi):
    calculation = pi * (radius**2)
    return calculation


pi = 3.14
result = area(10, pi)
print("Area of the pond is ", int((result)), "meters")

sqaure_meter = 1.4
total_water = result * sqaure_meter
print("Total water of the pond is ", int((total_water)), "meters")
