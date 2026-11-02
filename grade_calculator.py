name = input("Enter student's name: ")

subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

print()

if (subject1 < 0 or subject1 > 100 or
    subject2 < 0 or subject2 > 100 or
    subject3 < 0 or subject3 > 100):

    print("Invalid marks! Marks must be between 0 and 100.")

else:
    average = (subject1 + subject2 + subject3) / 3

    if average >= 80 and average <= 100:
        grade = "A+"
    elif average >= 70 and average <= 79:
        grade = "A"
    elif average >= 60 and average <= 69:
        grade = "A-"
    elif average >= 50 and average <= 59:
        grade = "B"
    elif average >= 40 and average <= 49:
        grade = "C"
    else:
        grade = "F"


    print(f"Student Name: {name}")
    print(f"Average Marks: {average:.2f}")
    print(f"Final Grade: {grade}")
