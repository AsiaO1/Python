# Error Handling with try/except
calculation_to_minutes = 24 * 60
name_of_unit = "minutes"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_minutes} {name_of_unit}"


def validate_and_execute():
    try:

        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_days = days_to_units(user_input_number)
            print(calculated_days)
        elif user_input_number == 0:
            return 'You entered 0, please enter a valid number!'
        else:
            print("You entered a negative number, so no conversion for you!")
    except ValueError:
        print("Your input is not a number. Don't ruin my program!")


user_input = input("Please enter number of days and we will covert it to minutes!\n")
validate_and_execute()