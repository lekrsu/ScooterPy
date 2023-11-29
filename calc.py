import math

def calculate_field_weakening_flux(initial, current_speed, field_weakening_start_speed, variable):
    """Calculate the field weakening flux based on current speed and other parameters."""
    if current_speed <= field_weakening_start_speed:
        return 0.0
    else:
        return initial + (current_speed - field_weakening_start_speed) * (variable / 1000)

def calculate_charge_percentage(voltage, num_cells):
    """Calculate the charge percentage of a battery based on voltage and number of cells."""
    min_voltage = 3.0
    max_voltage = 4.2
    return ((voltage - min_voltage * num_cells) / ((max_voltage - min_voltage) * num_cells)) * 100

def calculate_max_battery_voltage(Radc):
    """Calculate the maximum battery voltage based on Radc value."""
    if Radc > 0:
        max_voltage = 3.3
        R1 = 10000
        return (max_voltage * (Radc + R1)) / R1
    else:
        return None

def calculate_shunt_resistor(R1, current_max, desired_current):
    """Calculate the shunt resistor value for a desired current."""
    if R1 <= 0 or current_max <= 0:
        return None
    Ra = (R1 / current_max) * desired_current
    total_shunt_value = (R1 * Ra) / (R1 + Ra)
    return Ra, total_shunt_value

def main():
    print("Please select an option:")
    print("1. Calculate field weakening flux")
    print("2. Calculate charge percentage")
    print("3. Calculate max battery voltage")
    print("4. Calculate shunt resistor for desired current")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            initial = float(input("Enter the initial value of the field weakening flux: "))
            current_speed = float(input("Enter the current speed of the scooter: "))
            field_weakening_start_speed = float(input("Enter the speed at which field weakening should start: "))
            variable = float(input("Enter the parameter that influences the rate of flux increase: "))
            field_weakening_flux = calculate_field_weakening_flux(initial, current_speed, field_weakening_start_speed, variable)
            print("The field weakening flux is:", field_weakening_flux)
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

    elif choice == "2":
        try:
            battery_voltage = float(input("Enter the battery voltage (in volts): "))
            num_cells = int(input("Enter the number of cells in series: "))
            charge_percent = calculate_charge_percentage(battery_voltage, num_cells)
            print(f"Charge percentage for a {battery_voltage}-volt battery: {charge_percent:.2f}%")
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

    elif choice == "3":
        try:
            Radc = float(input("Enter the Radc value: "))
            max_battery_voltage = calculate_max_battery_voltage(Radc)
            if max_battery_voltage is not None:
                print(f"Max Battery Voltage (Vmax): {max_battery_voltage:.2f}V")
            else:
                print("Invalid Radc value. Please enter a value greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

    elif choice == "4":
        try:
            R1 = float(input("Enter the initial shunt resistor value (R1) in ohms: "))
            current_max = float(input("Enter the maximum current (I) in amperes: "))
            desired_current = float(input("Enter the desired maximum current (Ia) in amperes: "))
            resistor_values = calculate_shunt_resistor(R1, current_max, desired_current)
            if resistor_values:
                Ra, total_shunt_value = resistor_values
                print(f"The calculated shunt resistor value (Ra) is: {Ra:.9f} ohms")
                print(f"The total shunt value to achieve {desired_current}A is: {total_shunt_value:.9f} ohms")
            else:
                print("Invalid input. Please check your values.")
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
