def reverseinteger():
    integer = int(input("Enter an integer: "))
   # reversed_integer = 0
    while integer > 0:
        digit = integer % 10
        reversed_integer = (reversed_integer * 10) + digit
        integer //= 10
    print(f"Reversed integer: {reversed_integer}")
    

reverseinteger()
    