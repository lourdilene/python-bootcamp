height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

weight_int = int(weight)
height_float = float(height)

bmi = weight_int/(height_float**2)

print(int(bmi))