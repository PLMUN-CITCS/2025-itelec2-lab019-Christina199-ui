def get_student_score():
    """Function to get student's score."""
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:  # Make sure the score is in the correct range.
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_grade(score):
    """Function to calculate grade based on score."""
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
        
score = get_student_score()  # Get the student's score
grade = calculate_grade(score)  # Calculate the grade
print(f"Your Grade is: {grade}")  # Output the grade
