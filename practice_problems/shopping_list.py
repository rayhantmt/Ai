def shopping_list_manager():
    # Initialize an empty list to store the shopping items
    shopping_list = []
    
    print("Welcome to Shopping List Manager!")
    print("Type your items one by one. When you are finished, type 'done'.\n")
    
    while True:
        # Take input from the user and strip leading/trailing whitespace
        item = input("Add item: ").strip()
        
        # Check if the user is finished (case-insensitive for better UX)
        if item.lower() == 'done':
            break
        
        # Prevent adding empty inputs if the user just presses Enter
        if item == "":
            print("Please enter a valid item name.")
            continue
            
        # Add the item to our list
        shopping_list.append(item)
    
    # Display the results
    print("\n--- Your Shopping List ---")
    if not shopping_list:
        print("Your shopping list is empty.")
    else:
        # Loop through and print each item with a list number
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
            
        # Display the total count using len()
        print("--------------------------")
        print(f"Total number of items: {len(shopping_list)}")

# Run the program
if __name__ == "__main__":
    shopping_list_manager()