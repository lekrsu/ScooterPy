import math

def calculate_field_weakening_flux(initial, current_speed, field_weakening_start_speed, variable):
    if current_speed <= field_weakening_start_speed:
        field_weakening_flux = 0.0
    else:
        field_weakening_flux = initial + (current_speed - field_weakening_start_speed) * (variable / 1000)
    return field_weakening_flux


def calculate_charge_percentage(voltage, num_cells):
    min_voltage = 3.0
    max_voltage = 4.2
    charge_percentage = ((voltage - min_voltage * num_cells) / ((max_voltage - min_voltage) * num_cells)) * 100
    return charge_percentage

def calculate_max_battery_voltage():
    Radc = float(input("Enter the Radc value: "))

    if not math.isnan(Radc):
        max_voltage = 3.3
        R1 = 10000
        Vmax = (max_voltage * (Radc + R1)) / R1
        print(f"Max Battery Voltage (Vmax): {Vmax:.2f}V")
    else:
        print("Please enter a valid Radc value.")

def calculate_shunt_resistor(current_max, desired_current):
    try:
        R1 = float(input("Enter the initial shunt resistor value (R1) in ohms: "))
        if R1 <= 0:
            raise ValueError("Shunt resistor value must be greater than zero.")
        
        shunt_resistor = (R1 / current_max) * desired_current
        print(f"The shunt resistor value (Ra) to achieve {desired_current}A is: {shunt_resistor:} ohms")
    except ValueError as e:
        print(f"Invalid input. {e}")



def main():
    print("Please select an option:")
    print("1. Calculate field weakening flux")
    print("2. Calculate charge percentage")
    print("3. Calculate max battery voltage")
    print("4. Calculate shunt resistor for desired current")    

    choice = input("Enter your choice: ")

    if choice == "1":
        initial = float(input("Enter the initial value of the field weakening flux: "))
        current_speed = float(input("Enter the current speed of the scooter: "))
        field_weakening_start_speed = float(input("Enter the speed at which field weakening should start: "))
        variable = float(input("Enter the parameter that influences the rate of flux increase: "))

        field_weakening_flux = calculate_field_weakening_flux(initial, current_speed, field_weakening_start_speed, variable)

        print("The field weakening flux is: ", field_weakening_flux)
    elif choice == "2":
        try:
            battery_voltage = float(input("Enter the battery voltage (in volts): "))
            num_cells = int(input("Enter the number of cells in series: "))

            charge_percent = calculate_charge_percentage(battery_voltage, num_cells)
            print(f"Charge percentage for a {battery_voltage}-volt battery: {charge_percent:.2f}%")
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")
    elif choice == "3":
        calculate_max_battery_voltage()
    elif choice == "4":
        calculate_shunt_resistor(float(input("Enter the maximum current (I) in amperes: ")),
                                 float(input("Enter the desired maximum current (Ia) in amperes: ")))

    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()