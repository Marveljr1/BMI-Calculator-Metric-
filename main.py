#BMI Calaculation
print("Welcome to the BMI Calaculation")
print("Please enter your height then weight to see your BMI Calaculation")
height = input()
weight = input()

weight_as_int = int(weight)
height_as_float = float(height)

bmi = (weight_as_int / height_as_float ** 2)

print(int(bmi))