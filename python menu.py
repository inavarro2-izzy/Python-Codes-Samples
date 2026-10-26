
# Module 4 Team Assignment
# Student: Israel Navarro
# Project: School Technology Help Desk
# Description: A menu-driven program using if, elif,
# else, and a while loop.

print("Welcome to the School Technology Help Desk!")

while True:
    print("\n========== MAIN MENU ==========")
    print("1. Reset Password")
    print("2. Internet Connection")
    print("3. Printer Problems")
    print("4. Computer Troubleshooting")
    print("5. Software Installation")
    print("6. Email Support")
    print("7. Student Chromebook Help")
    print("8. Classroom Technology")
    print("9. Contact IT Support")
    print("0. Exit")
    print("===============================")

    choice = input("Enter your choice (0-9): ")

    if choice == "1":
        print("You selected 1: Reset Password.")
    elif choice == "2":
        print("You selected 2: Internet Connection.")
    elif choice == "3":
        print("You selected 3: Printer Problems.")
    elif choice == "4":
        print("You selected 4: Computer Troubleshooting.")
    elif choice == "5":
        print("You selected 5: Software Installation.")
    elif choice == "6":
        print("You selected 6: Email Support.")
    elif choice == "7":
        print("You selected 7: Student Chromebook Help.")
    elif choice == "8":
        print("You selected 8: Classroom Technology.")
    elif choice == "9":
        print("You selected 9: Contact IT Support.")
    elif choice == "0":
        print("You selected 0: Exit. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number from 0 to 9.")
