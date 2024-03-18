# task 1
height = float(input("Please enter your height in meters: "))
weight = float(input("Please enter your weight in kilograms: "))


def BMI(height, weight):
    bmi = weight / (height * height)
    if bmi >= 30:
        answer = "Obesity"
    elif bmi >= 25:
        answer = "Overweight"
    elif bmi >= 18.5 and bmi < 25:
        answer = "Normal"
    else:
        answer = "Underweight"
    return answer, bmi

answer, calculated_bmi = BMI(height, weight)
print("Your BMI answer is:", answer)
print("Your calculated BMI value is:", calculated_bmi)
