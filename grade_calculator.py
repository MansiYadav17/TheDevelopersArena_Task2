def get_grade_info(marks):
    """
    Function to determine the grade and an encouraging message 
    based on the marks provided.
    """
    if marks >= 90:
        return "A", "Excellent work! You're a superstar!"
    elif marks >= 80:
        return "B", "Very Good! Keep it up!"
    elif marks >= 70:
        return "C", "Good job! You're doing well."
    elif marks >= 60:
        return "D", "You passed, but there is room for improvement."
    else:
        return "F", "Don't give up! Study harder and you will improve."

def main():
    print("--- Student Grade Calculator ---")
    
    # Day 2: Create Input System
    name = input("Enter student name: ").strip()
    
    # Day 4: Add Validation & Loop to handle invalid inputs
    while True:
        try:
            user_input = input("Enter marks (0-100): ")
            marks = float(user_input)
            
            # Check marks range
            if 0 <= marks <= 100:
                break
            else:
                print("Error: Please enter a value between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a numerical value for marks.")

    # Day 3 & 5: Grading Logic & Final Program Assembly
    grade, message = get_grade_info(marks)

    print(f"\n📊 RESULT FOR {name.upper()}:")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message} 👍")

if __name__ == "__main__":
    main()
