def calculate_voltage(current, resistance):
    return current * resistance

def calculate_current(voltage, resistance):
    if resistance == 0:
        return "Error: Resistance cannot be zero."
    return voltage / resistance

def calculate_resistance(voltage, current):
    if current == 0:
        return "Error: Current cannot be zero."
    return voltage / current

def ohms_law_calculator():
    print("What would you like to calculate?")
    print("1. Voltage (V)")
    print("2. Current (I)")
    print("3. Resistance (R)")
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        current = float(input("Enter the current (I) in amperes: "))
        resistance = float(input("Enter the resistance (R) in ohms: "))
        voltage = calculate_voltage(current, resistance)
        print(f"The voltage (V) is: {voltage:.2f} volts")
    
    elif choice == "2":
        voltage = float(input("Enter the voltage (V) in volts: "))
        resistance = float(input("Enter the resistance (R) in ohms: "))
        current = calculate_current(voltage, resistance)
        if isinstance(current, str):
            print(current)
        else:
            print(f"The current (I) is: {current:.2f} amperes")
    
    elif choice == "3":
        voltage = float(input("Enter the voltage (V) in volts: "))
        current = float(input("Enter the current (I) in amperes: "))
        resistance = calculate_resistance(voltage, current)
        if isinstance(resistance, str):
            print(resistance)
        else:
            print(f"The resistance (R) is: {resistance:.2f} ohms")
    
    else:
        print("Invalid choice! Please select 1, 2, or 3.")

ohms_law_calculator()
