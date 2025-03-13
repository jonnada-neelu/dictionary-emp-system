# Solution
#Employee management using dictionaries

def add_employee(employees):
    emp_id = input("Enter Employee ID: ")
    if emp_id in employees:
        print("Employee ID already exists! Try again.")
        return
    
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    if age <= 0:
        print("Invalid age! Enter a positive integer.")
        return
    
    department = input("Enter Department: ")
    employees[emp_id] = {"name": name, "age": age, "department": department}
    print("Employee added successfully!")

def remove_employee(employees):
    emp_id = input("Enter Employee ID to remove: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee removed successfully!")
    else:
        print("Employee ID not found!")

def update_employee(employees):
    emp_id = input("Enter Employee ID to update: ")
    if emp_id not in employees:
        print("Employee ID not found!")
        return
    
    print("Leave field blank to keep existing value.")
    new_name = input("Enter New Name: ")
    if new_name:
        employees[emp_id]["name"] = new_name
    
    new_age = input("Enter New Age: ")
    if new_age:
            new_age = int(new_age)
            employees[emp_id]["age"] = new_age
            if new_age <= 0:
             print("Invalid age! Enter a positive integer.")
            return
    
    new_department = input("Enter New Department: ")
    if new_department:
        employees[emp_id]["department"] = new_department
    
    print("Employee details updated successfully!")

def search_employee(employees):
    choice = input("Search by (1) Employee ID or (2) Name: ")
    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        if emp_id in employees:
            print(f"{emp_id}: {employees[emp_id]}")
        else:
            print("Employee not found!")
    elif choice == "2":
        name = input("Enter Name: ").lower()
        found = False
        for emp_id, details in employees.items():
            if details["name"].lower() == name:
                print(f"{emp_id}: {details}")
                found = True
        if not found:
            print("Employee not found!")
    else:
        print("Invalid choice!")

import operator

def sort_employees(employees):
    options = {"1": "name", "2": "age", "3": "department"}
    choice = input("Sort by (1) Name, (2) Age, (3) Department: ")

    if choice in options:
        key = options[choice]
        sorted_emps = sorted(employees.items(), key=operator.itemgetter(1, key) if key == "age" 
        else lambda x: x[1][key].lower())
        for emp_id, details in sorted_emps:
            print(f"{emp_id}: {details['name']}, {details['age']} years, {details['department']}")
    else:
        print("Invalid choice!")
        return
    
    for emp_id, details in sorted_emps:
        print(f"{emp_id}: {details}")

def main():

    employees = {}
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Remove Employee")
        print("3. Update Employee")
        print("4. Search Employee")
        print("5. Sort Employees")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            add_employee(employees)
        elif choice == "2":
            remove_employee(employees)
        elif choice == "3":
            update_employee(employees)
        elif choice == "4":
            search_employee(employees)
        elif choice == "5":
            sort_employees(employees)
        elif choice == "6":
            print("Exiting Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
