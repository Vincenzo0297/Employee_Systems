class Employee:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def getID(self):
        return self.id

    def getName(self):
        return self.name

    def getEmail(self):
        return self.email
    
    def setName(self, name):
        self.name = name

    def setEmail(self, email):
        self.email = email
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Email: {self.email}"


def main():
    employee_list = []
    while True:
        print("\n1) Add Employee")
        print("2) View Employee")
        print("3) Update Employee")
        print("4) Delete Employee")
        print("5) View All Employees")
        print("6) Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_employee(employee_list)
        elif choice == '2':
            view_employee(employee_list)  # You might want to implement this function
        elif choice == '3':
            update_employee(employee_list)  # You might want to implement this function
        elif choice == '4':
            delete_employee(employee_list)  # You might want to implement this function
        elif choice == '5':
            view_all_employees(employee_list)  # You might want to implement this function
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")


def add_employee(employee_list):
    while True:
        try:
            ID = input("Enter ID: ")
            if any(e.getID() == ID for e in employee_list):
                print("ID already exists!")
                break

            Name = input("Enter Name: ")
            if any(e.getName() == Name for e in employee_list):
                print("Name already exists!")
                break

            Email = input("Enter Email: ")
            if any(e.getEmail() == Email for e in employee_list):
                print("Email already exists!")
                break

            confirm = input("Press 'y' to add Employee: ")
            if confirm.lower() == 'y':
                employee = Employee(ID, Name, Email)
                employee_list.append(employee)
                print(f"{employee} has been added.")
            else:
                print("Employee not added.")
            break
        except Exception as e:
            print(f"Error: {e}")
            break

def view_employee(employee_list):
    ID = input("Enter ID: ")
    for employee in employee_list:
        if employee.getID() == ID:
            print(employee)
            return
    print("Employee not found.")


def update_employee(employee_list):
    ID = input("Enter ID: ")
    for employee in employee_list:
        if employee.getID() == ID:
            Name = input("Enter new Name: ")
            Email = input("Enter new Email: ")
            employee.setName(Name)
            employee.setEmail(Email)
            print(f"Updated employee details: {employee}")
            return
    print("Employee not found.")


def delete_employee(employee_list):
    ID = input("Enter ID: ")
    for employee in employee_list:
        if employee.getID() == ID:
            employee_list.remove(employee)
            print("Employee deleted successfully!")
            return
    print("Employee not found.")


def view_all_employees(employee_list):
    if not employee_list:
        print("No employees found.")
    else:
        for employee in employee_list:
            print(employee)


if __name__ == "__main__":
    main()
