import os
import json

# Check at Create tayo nang StudentInfo folder, if di siya nag exist 
# automatic siya gagawa nang directory sa katabing file nang python.
# If yung folder na yun is nag exist na Lets begin the first step.

if not os.path.exists('StudentInfo'):
    os.makedirs('StudentInfo')

# First gawa tayo main Menu
while True:
    print("\nStudent Enrollment System Menu:")
    print("1. Add Student")
    print("2. View Student")
    print("3. Exit")
    choice = input("Enter no. (1/2/3): ")

    if choice == '1':
        add_students()
    elif choice == '2':
        view_students()
    elif choice == '3':
        print("Thank you for using our system!")
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# Gawa tayo nang functions para sa Add Student.
def add_students():
    student_info = {}
    full_name = input("Enter Full Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    email = input("Enter Email: ")

    student_info['Full Name'] = full_name
    student_info['Age'] = age
    student_info['Gender'] = gender
    student_info['Email'] = email

    # Check natin if yung student eh already exist na sa folder
    # natin, if hindi pa dun natin isasave, if yung student is nag exist na
    # di na natin siya i-a-allowed mag save nang same information sa loob nang folder natin.

    if not os.path.exists(f"StudentInfo/{full_name}.json"):
        with open(f"StudentInfo/{full_name}.json", 'w') as file:
            json.dump(student_info, file)
        print(f"Student {full_name} added successfully!")
    else:
        print(f"Student {full_name} already exists.")

# In this next section of a block of code, gagawa tayo nang 
# view function sa lahat nang student, ka-sabay nun 
# mag-peperform tayo nang update and delete functions.
def view_students():
    student_files = os.listdir('StudentInfo')
    if not student_files:
        print("No students in the system.")
        return
    
    for s, student_file in enumerate(student_files, start=1):
        print(f"{s}. {student_file[:-5]}")

    choice = int(input("Enter the number of the student you want to\nView\nUpdate\nDelete\n(0 to go back): "))
    if choice == 0:
        return
    
    selected_student = student_files[choice - 1]
    with open(f"StudentInfo/{selected_student}", 'r') as file:
        student_info = json.load(file)

    print(f"Full Name: {student_info['Full Name']}")
    print(f"Age: { student_info['Age']}")
    print(f"Gender: { student_info['Gender']}")
    print(f"Email: { student_info['Email']}")

    update_or_delete = input("Do you want to update (U) or delete (D) this student? (Enter U/D): ").upper()
    if update_or_delete == 'U':
        update_student(selected_student, student_info)
    elif update_or_delete == 'D':
        delete_student(selected_student)

# Gawa tayo dito nang update function para sa student if 
# ever gusto nila i-update yung infromation nila.
def update_student(file_name, student_info):
    print("Update Student Information:")
    new_name = input("Enter New Name: ")
    new_age = input("Enter New Age: ")
    new_gender = input("Enter New Gender: ")
    new_email = input("Enter New Email: ")

    student_info['Full Name'] = new_name
    student_info['Age'] = new_age
    student_info['Gender'] = new_gender
    student_info['Email'] = new_email

    with open(f"StudentInfo/{file_name}", 'w') as file:
        json.dump(student_info, file)

    print("Student Information update successfully!")

# For the last function ay ang delete function para sa student information.
def delete_student(file_name):
    os.remove(f"StudentInfo/{file_name}")
    print("Student Information deleted successfully!")