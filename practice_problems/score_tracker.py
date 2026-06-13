def score_tracker():
    # Initialize an empty dictionary to store names and scores
    scores_dict = {}
    
    print("Enter student names and scores. Type 'stop' as the name to finish.\n")
    
    while True:
        # Take the student's name as input
        name = input("Enter student's name: ").strip()
        
        # Check for the exit condition (case-insensitive for a better user experience)
        if name.lower() == 'stop':
            break
            
        # Take the score as input and convert it to an integer or float
        try:
            score = float(input(f"Enter score for {name}: "))
        except ValueError:
            print("Invalid input. Please enter a numerical value for the score.")
            continue
            
        # Store or update the score in the dictionary
        scores_dict[name] = score
        print() # Print a blank line for clean formatting

    # Print out all stored students and their scores
    print("\n--- Final Student Scores ---")
    if not scores_dict:
        print("No student data recorded.")
    else:
        for name, score in scores_dict.items():
            print(f"Student: {name} | Score: {score}")

# Run the program
if __name__ == "__main__":
    score_tracker()