###   *If/else*
# Python Comparison Operators:
# == --> equal
# != --> not equal
# > --> greater than
# < --> less than
# >= --> greater than or equal
# <= --> less than or equal

# 1. first user enters and input, which is converted to number, we pass that number to the function
# (input can be a positive number/negative number/ or even a string)
# 1. return function is executed
# 2. return value is assigned to variable
# 3. variable value is printed to standard output
calculation_to_minutes = 24 * 60
name_of_unit = "minutes"


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_minutes} {name_of_unit}"
    elif num_of_days == 0:
        return 'You entered 0, please enter a valid number!'


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_days = days_to_units(user_input_number)
        print(calculated_days)
    else:
        print("Your input is not a number. Don't ruin my program!")


user_input = input("Please enter number of days and we will covert it to minutes!\n")
validate_and_execute()