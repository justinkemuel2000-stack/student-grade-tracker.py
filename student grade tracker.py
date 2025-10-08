Student_Ids = []
Student_Data = {}
Unique_Subject = set()

print("----Student Grade Tracker----")
print("1.Add student grade")
print("2.View all students")
print("3.View unique subject")
print("4.Exit")

choice = input("Enter your choice: ")

if choice == "1":
    print("Add student grade")
    name = input("Enter your name: ")
    grade = float(input("Enter your age: "))
    subject = input("Enter your subject: ")
    student_info = (name, grade, subject) # Tuple
    student_id = len(Student_Ids) + 1 # List
    Student_Ids.append(student_id)
    Student_Data[student_id] = student_info # Dict
    Unique_Subject.add(subject) # Set
    print("Successfully Added!")

elif choice == "2":
    print("View all students")
    for sid, info in Student_Data.items():
        print(f"Id: {sid}, Name: {info[0]}, Grade: {info[1]}, Subject: {info[2]}")

elif choice == "3":
    print("View unique subject")
    for ust in Unique_Subject:
        print(ust)

elif choice == "4":
    print("Exit")

else:
    print("Invalid input")
