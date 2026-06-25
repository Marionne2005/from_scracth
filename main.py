from repository import Operations
from models import Student

def main():
    repo = Operations()
     
    while True:
        print("\n=== Student Management System ===")
        print("1. Add a student")
        print("2. View all students")
        print("3. Search student by name")
        print("4. Update GPA")
        print("5. Delete student")
        print("6. View average GPA")
        print("7. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            gpa = float(input("Enter GPA: "))
            while gpa < 0.0 or gpa > 4.0:
                print("GPA must be between 0.0 and 4.0")
                gpa = float(input("Enter GPA: "))
            program = input("Enter program: ")
            student = Student(name, email, gpa, program)
            repo.create_student(student)
            print("Student added successfully!")
        
        elif choice == '2':
            students = repo.get_all_students()
            for student in students:
                print(student)
        
        elif choice == '3':
            name = input("Enter name to search: ")
            students = repo.search_by_name(name)
            for student in students:
                print(student)

        elif choice == '4':   
            student_id = int(input("Enter student ID to update GPA: "))
            new_gpa = float(input("Enter new GPA: "))
            while new_gpa < 0.0 or new_gpa > 4.0:
                print("GPA must be between 0.0 and 4.0")
                new_gpa = float(input("Enter new GPA: "))
            repo.update_gpa(student_id, new_gpa)
            print("GPA updated successfully!")

        elif choice == '5':
            student_id = int(input("Enter student ID to delete: "))
            repo.delete_student(student_id)
            print("Student deleted successfully!")
        elif choice == '6':
            avg_gpa = repo.get_average_gpa()
            print(f"Average GPA: {avg_gpa:.2f}")

        elif choice == '7':
            print("Exiting...")
            break             
    repo.close()

if __name__ == "__main__":
    main()