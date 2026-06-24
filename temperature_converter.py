

temp = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C/F/K): ").upper()

if unit == "C":
fahrenheit = (temp * 9/5) + 32
kelvin = temp + 273.15

print("\nConverted Temperatures:")
print("Fahrenheit =", round(fahrenheit, 2), "°F")
print("Kelvin =", round(kelvin, 2), "K")

elif unit == "F":
celsius = (temp - 32) * 5/9
kelvin = celsius + 273.15

print("\nConverted Temperatures:")
print("Celsius =", round(celsius, 2), "°C")
print("Kelvin =", round(kelvin, 2), "K")

elif unit == "K":
celsius = temp - 273.15
fahrenheit = (celsius * 9/5) + 32

print("\nConverted Temperatures:")
print("Celsius =", round(celsius, 2), "°C")
print("Fahrenheit =", round(fahrenheit, 2), "°F")

else:
print("Invalid unit! Please enter C, F, or K.")
