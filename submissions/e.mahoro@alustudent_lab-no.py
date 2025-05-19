# aluStudentEmail_Lab-1.py
# Programming Concepts Used:
# - Data Structures: Lists (to store assignments), Classes (for Assignment and GradeCalculator)
# - Loops: While loops (for input validation and adding assignments)
# - Object-Oriented Programming: Classes and objects to structure code
# - Conditional Logic: If statements to determine pass/fail status and validate inputs
# - Input/Output: User input for assignment details and printing results

class Assignment:
    def __init__(self, name, category, weight, grade):
        self.name = name
        self.category = category
        self.weight = weight
        self.grade = grade

    def weighted_grade(self):
        return (self.grade * self.weight) / 100


class GradeCalculator:
    def __init__(self):
        self.assignments = []

    def add_assignment(self):
        name = input("Enter assignment name: ")
        category = input("Enter assignment category (Formative/Summative): ").strip().capitalize()
        while category not in ['Formative', 'Summative']:
            print("Invalid category. Please enter 'Formative' or 'Summative'.")
            category = input("Enter assignment category (Formative/Summative): ").strip().capitalize()

        weight = float(input("Enter assignment weight (percentage): "))
        while weight < 0 or weight > 100:
            print("Invalid weight. Please enter a value between 0 and 100.")
            weight = float(input("Enter assignment weight (percentage): "))

        grade = float(input("Enter grade obtained (out of 100): "))
        while grade < 0 or grade > 100:
            print("Invalid grade. Please enter a value between 0 and 100.")
            grade = float(input("Enter grade obtained (out of 100): "))

        self.assignments.append(Assignment(name, category, weight, grade))

    def calculate_totals(self):
        total_weighted_formative = sum(a.weighted_grade() for a in self.assignments if a.category == 'Formative')
        total_weighted_summative = sum(a.weighted_grade() for a in self.assignments if a.category == 'Summative')
        total_weight = sum(a.weight for a in self.assignments)
        
        if total_weight == 0:
            return 0, 0, 0

        average_formative = total_weighted_formative / (total_weight if total_weight > 0 else 1)
        average_summative = total_weighted_summative / (total_weight if total_weight > 0 else 1)

        return total_weighted_formative, total_weighted_summative, average_formative, average_summative

    def calculate_gpa(self):
        total_weighted_grades = sum(a.weighted_grade() for a in self.assignments)
        total_weight = sum(a.weight for a in self.assignments)
        
        if total_weight == 0:
            return 0

        gpa = (total_weighted_grades / total_weight) * 5 / 100
        return gpa


def main():
    calculator = GradeCalculator()

    while True:
        calculator.add_assignment()
        more = input("Do you want to add another assignment? (yes/no): ").strip().lower()
        if more != 'yes':
            break

    total_formative, total_summative, avg_formative, avg_summative = calculator.calculate_totals()
    gpa = calculator.calculate_gpa()

    print("\nResults:")
    print(f"Total Weighted Formative Grade: {total_formative:.2f}")
    print(f"Total Weighted Summative Grade: {total_summative:.2f}")
    print(f"GPA: {gpa:.2f}")

    if avg_formative < 50 or avg_summative < 50:
        print("You have failed the course and must repeat it.")
    else:
        print("You have passed the course.")


if __name__ == "__main__":
    main()
