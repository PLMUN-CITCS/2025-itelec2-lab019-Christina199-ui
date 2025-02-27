def get_student_score() -> float:
    """Function to get the student's score."""
	
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:  # Ensure the score is within the valid range.
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_grade(score: float) -> str:
    """Function to calculate the letter grade based on the student's score."""
	
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

if __name__ == "__main__":
    score = get_student_score()  # Get the student's score.
    grade = calculate_grade(score)  # Calculate the grade based on the score.
    print(f"Your Grade is: {grade}")  # Output the grade.
