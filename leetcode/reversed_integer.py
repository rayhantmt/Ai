def reverseinteger():
    integer = int(input("Enter an integer: "))

    # 1. Create the variable to hold our answer
    reversed_integer = 0

    # 2. Check if the number is negative.
    # If it is, remember it, and turn the integer positive!
    is_negative = False
    if integer < 0:
        is_negative = True
        integer = -integer  # Converts e.g., -123 into 123

    # 3. This single loop handles the math for ALL numbers now
    while integer > 0:
        digit = integer % 10  # Grabs the last digit
        reversed_integer = (reversed_integer * 10) + digit  # Pushes it to the answer
        integer //= 10  # Chops off the last digit

    # 4. If the original number was negative, make the answer negative
    if is_negative:
        reversed_integer = -reversed_integer

    print(f"Reversed integer: {reversed_integer}")


# Run the function
reverseinteger()