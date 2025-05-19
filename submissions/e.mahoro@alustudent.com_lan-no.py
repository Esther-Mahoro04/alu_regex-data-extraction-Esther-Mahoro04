# aluStudentEmail_Lab-1.py
# Programming Concepts Used:
# - Data Structures: Lists (to store assignments), Classes (for Assignment and GradeCalculator)
# - Loops: While loops (for input validation and adding assignments)
# - Object-Oriented Programming: Classes and objects to structure code
# - Conditional Logic: If statements to determine pass/fail status and validate inputs
# - Input/Output: User input for assignment details and printing results

# Class to represent an individual assignment
class Assignment:
    def __init__(self, name, category, weight, grade):
        # Initialize the assignment with its attributes
        self.name = name
        self.category = category  # Formative or Summative
        self.weight = weight      # Weight of the assignment as a percentage
        self.grade = grade        # Grade obtained (out of 100)

    def weighted_grade(self):
        # Calculate the weighted grade for the assignment
        return (self.grade * self.weight) / 100

# Class to handle grade calculations for multiple assignments
class GradeCalculator:
    def __init__(self):
        # Initialize an empty list to store assignments
        self.assignments = []

    def add_assignment(self):
        # Collect assignment details from the user
        name = input("Enter assignment name: ")
        
        # Input validation for assignment category
        category = input("Enter assignment category (Formative/Summative): ").strip().capitalize()
        while category not in ['Formative', 'Summative']:
            print("Invalid category. Please enter 'Formative' or 'Summative'.")
            category = input("Enter assignment category (Formative/Summative): ").strip().capitalize()

        # Input validation for weight
        weight = float(input("Enter assignment weight (percentage): "))
        while weight < 0 or weight > 100:
            print("Invalid weight. Please enter a value between 0 and 100.")
            weight = float(input("Enter assignment weight (percentage): "))

        # Input validation for grade
        grade = float(input("Enter grade obtained (out of 100): "))
        while grade < 0 or grade > 100:
            print("Invalid grade. Please enter a value between 0 and 100.")
            grade = float(input("Enter grade obtained (out of 100): "))

        # Create a new Assignment object and add it to the list
        self.assignments.append(Assignment(name, category, weight, grade))

    def calculate_totals(self):
        # Calculate total weighted grades for formative and summative assignments
        total_weighted_formative = sum(a.weighted_grade() for a in self.assignments if a.category == 'Formative')
        total_weighted_summative = sum(a.weighted_grade() for a in self.assignments if a.category == 'Summative')
        total_weight = sum(a.weight for a in self.assignments)
        
        # Avoid division by zero
        if total_weight == 0:
            return 0, 0, 0

        # Calculate average grades for each category
        average_formative = total_weighted_formative / total_weight
        average_summative = total_weighted_summative / total_weight

        return total_weighted_formative, total_weighted_summative, average_formative, average_summative

    def calculate_gpa(self):
        # Calculate the overall GPA based on weighted grades
        total_weighted_grades = sum(a.weighted_grade() for a in self.assignments)
        total_weight = sum(a.weight for a in self.assignments)
        
        # Avoid division by zero
        if total_weight == 0:
            return 0

        # GPA calculation normalized to a scale of 5
        gpa = (total_weighted_grades / total_weight) * 5 / 100
        return gpa

# Main function to run the program
def main():
    calculator = GradeCalculator()

    # Loop to allow multiple assignments to be added
    while True:
        calculator.add_assignment()
        more = input("Do you want to add another assignment? (yes/no): ").strip().lower()
        if more != 'yes':
            break

    # Calculate totals and GPA
    total_formative, total_summative, avg_formative, avg_summative = calculator.calculate_totals()
    gpa = calculator.calculate_gpa()

    # Display results to the user
    print("\nResults:")
    print(f"Total Weighted Formative Grade: {total_formative:.2f}")
    print(f"Total Weighted Summative Grade: {total_summative:.2f}")
    print(f"GPA: {gpa:.2f}")

    # Determine pass/fail status based on averages
    if avg_formative < 50 or avg_summative < 50:
        print("You have failed the course and must repeat it.")
    else:
        print("You have passed the course.")

# Entry point of the program
if __name__ == "__main__":
    main()
