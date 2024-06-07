def calculate_new_shunt_value(existing_shunt, existing_current_limit, new_current_limit):
    new_shunt = existing_shunt * (existing_current_limit / new_current_limit)
    return new_shunt

def calculate_parallel_shunt_value(existing_shunt, existing_current_limit, new_current_limit):
    total_desired_resistance = existing_shunt * (existing_current_limit / new_current_limit)
    parallel_resistor = (existing_shunt * total_desired_resistance) / (existing_shunt - total_desired_resistance)
    return parallel_resistor

def main():
    existing_shunt = float(input("Enter the existing shunt resistor value in ohms: "))
    existing_current_limit = float(input("Enter the existing current limit in amperes: "))
    new_current_limit = float(input("Enter the new desired current limit in amperes: "))

    new_shunt = calculate_new_shunt_value(existing_shunt, existing_current_limit, new_current_limit)
    print(f"New shunt value for replacement: {new_shunt:.10g} ohms")

    parallel_shunt = calculate_parallel_shunt_value(existing_shunt, existing_current_limit, new_current_limit)
    print(f"Additional shunt value for parallel addition: {parallel_shunt:.10g} ohms")

if __name__ == "__main__":
    main()
