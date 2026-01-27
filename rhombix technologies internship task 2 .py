students = {}  # dictionary to store student names and their grades

def calculate_average(mar):
    if len(mar) == 0:
        return 0
    return sum(mar) / len(mar)

while True:
    print("\n Student Grade Tracker ")
    print("1. Add student")
    print("2. Add grades")
    print("3. View student record")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_number = input("Enter your roll number: ")
        name = input("Enter your name: ")
        students[roll_number] = {"name": name, "grades": []}
        print("Student added successfully.")

    elif choice == "2":
        roll_number = input("Enter your roll number: ")
        if roll_number in students:
            subject_count = int(input("Enter number of subjects: "))
            students[roll_number]["grades"].clear()

            for i in range(subject_count):
                marks = float(input(f"Enter marks for subject {i+1}: "))
                students[roll_number]["grades"].append(marks)

            print("Grades added successfully.")
        else:
            print("Student not found.")

    elif choice == "3":
        roll_number = input("Enter your roll number: ")
        if roll_number in students:
            grades = students[roll_number]["grades"]
            average = calculate_average(grades)

            print("\nStudent Name:", students[roll_number]["name"])
            print("Grades:", grades)
            print("Average Marks:", average)
        else:
            print("Student not found.")

    elif choice == "4":
        print("Program exited.")
        break

    else:
        print("Invalid choice! Try again.")
