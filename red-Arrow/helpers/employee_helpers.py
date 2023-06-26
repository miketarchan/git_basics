from .system_helpers import save_to_file, get_file_data, save_all


def save(email, first_name, last_name, phone):
    new_employee = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
    }
    save_to_file(new_employee)


def get_all_employers():
    employees = get_file_data()
    for i in range(len(employees)):
        print(f'{i}: ')
        print(f'\t{employees[i]["email"]}')
        print(f'\t{employees[i]["first_name"]}')
        print(f'\t{employees[i]["last_name"]}')
        print(f'\t{employees[i]["phone"]}')


def get_employee_by_email(email):
    employees = get_file_data()
    for employee in employees:
        if employee["email"] == email:
            print(employee["email"])
            print(employee["first_name"])
            print(employee["last_name"])
            print(employee["phone"])


def update_employee_by_id(id, email, first_name, last_name, phone):
    employees = get_file_data()
    employees[int(id)] = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone
    }
    save_all(employees)
