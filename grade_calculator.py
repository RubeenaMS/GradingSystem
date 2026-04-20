def get_grade(score):
    if 90 <= score <= 100:
        return "A", "Excellent! You're a Star!"
    elif 80 <= score <= 89:
        return "B", "Very Good! Keep it up!"
    elif 70 <= score <= 79:
        return "C", "Good Job! You can do better!"
    elif 60 <= score <= 69:
        return "D", "Fair. You need to work harder!"
    elif 0 <= score <= 59:
        return "F", "Needs Improvement. Don't give up!"
    else:
        return "Invalid"
name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))

grade, message = get_grade(marks)

print(f"\n RESULT FOR {name.upper()}:")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")