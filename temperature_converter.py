
def celsius_to_others(temp):
    fahrenheit = (temp * 9/5) + 32
    kelvin = temp + 273.15
    return round(fahrenheit, 2), round(kelvin, 2)

def fahrenheit_to_others(temp):
    celsius = (temp - 32) * 5/9
    kelvin = celsius + 273.15
    return round(celsius, 2), round(kelvin, 2)

def kelvin_to_others(temp):
    celsius = temp - 273.15
    fahrenheit = (celsius * 9/5) + 32
    return round(celsius, 2), round(fahrenheit, 2)

def convert_temperature():
    try:
        temp = float(input("Enter the temperature value: "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return

    unit = input("Enter the unit (C/F/K): ").strip().upper()

    print("\nConverted Temperatures:")

    if unit == "C":
        f, k = celsius_to_others(temp)
        print(f"Fahrenheit = {f} °F")
        print(f"Kelvin     = {k} K")
    elif unit == "F":
        c, k = fahrenheit_to_others(temp)
        print(f"Celsius = {c} °C")
        print(f"Kelvin  = {k} K")
    elif unit == "K":
        if temp < 0:
            print("Invalid! Kelvin cannot be negative.")
            return
        c, f = kelvin_to_others(temp)
        print(f"Celsius    = {c} °C")
        print(f"Fahrenheit = {f} °F")
    else:
        print("Invalid unit! Please enter C, F, or K.")

if __name__ == "__main__":
    convert_temperature()
