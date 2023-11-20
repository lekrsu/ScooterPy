def calculate_field_weakening_flux(initial, current_speed, field_weakening_start_speed, variable):
    field_weakening_flux = initial + (current_speed - field_weakening_start_speed) * (variable / 1000)
    return field_weakening_flux

def calculate_charge_percentage(voltage, num_cells):
    min_voltage = 3.0
    max_voltage = 4.2
    charge_percentage = ((voltage - min_voltage * num_cells) / ((max_voltage - min_voltage) * num_cells)) * 100
    return charge_percentage

def main():
    print("Please select an option:")
    print("1. Calculate field weakening flux")
    print("2. Calculate charge percentage")

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
    else:
        print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
