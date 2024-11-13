def is_power(number, base):
    # Check for edge cases
    if base <= 1:
        return number == 1  # Only 1 is a power of any base <= 1
    if number < 1:
        return False  # Powers of positive integers are always >= 1

    # Keep dividing 'number' by 'base'
    while number > 1:
        if number % base != 0:  # If 'number' is not divisible by 'base'
            return False
        number //= base  # Divide 'number' by 'base'

    return number == 1  # If we reduced 'number' to 1, it's a power of 'base'

# User input for the number and base
number_input = input("Enter the number to check: ")
base_input = input("Enter the base: ")

# Check if inputs are valid integers
if number_input.isdigit() and base_input.isdigit():
    number = int(number_input)
    base = int(base_input)

    # Call the is_power function and print the result
    result = is_power(number, base)
    print(result)  # Output will be True or False
else:
    print("Please enter valid positive integers.")