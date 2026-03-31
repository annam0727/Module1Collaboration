#Module 2 Lab
#Anna Edwards
#Academic List Checker
#This app will allow student's to input first and last names and gpas to determine if they made an academic list at school

while True:
    last_name = input("Enter student's last name(or ZZZ to quit): ")

    if last_name == "ZZZ":
        print("Program ended.")
        break
    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    print("\nStudent:", first_name, last_name)

    if gpa >= 3.5:
        print("This student has made the Dean's List.")
    elif gpa >= 3.25:
        print("This student has made the Honor Roll.")
    else:
        print("This student did not qualify for either list.")

    print("-" * 40)