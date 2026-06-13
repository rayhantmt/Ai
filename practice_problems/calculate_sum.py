def calculate_sum():
    try:
        # Receive an integer input from the user
        n = int(input("Enter an integer (n): "))
        
        if n < 1:
            print("Please enter an integer greater than or equal to 1.")
            return

        # range(1, n + 1) includes numbers from 1 up to n
        total_sum = sum(range(1, n + 1))
        
        # Display the result
        print(f"The sum of numbers from 1 to {n} is: {total_sum}")
        
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

# Run Problem 1
if __name__ == "__main__":
    calculate_sum()