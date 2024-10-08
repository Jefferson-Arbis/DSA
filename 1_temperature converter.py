def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
    temperature = float(input("Enter the temperature: "))

    print("Select the conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        result = celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result:.2f}°F")
        
    elif choice == "2":
        result = fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is {result:.2f}°C")
        
    else:
        print("Invalid choice! Please select 1 or 2.")

temperature_converter()
