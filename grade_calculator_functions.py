def get_student_score() -> float:
    """Function to get the student's score."""
	
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:  # Ensure the score is within the valid range.
                return score
                
            print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_grade(score: float) -> str:
    """Function to calculate the letter grade based on the student's score."""
	
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
        
    return 'F'

def main():

    student_score = get_student_score()  # Get the student's score.
    grade = calculate_grade(grade_score)  # Calculate the grade based on the score.
    print(f"Your Grade is: {grade}")  # Output the grade.
    
if __name__ == "__main__":
    main()
