from .system_helpers import save_to_file, get_file_data, save_all


def save_employee(email, first_name, last_name, phone):
    new_employee = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
    }
    save_to_file(new_employee, "database/employees.json")


def get_all_employers():
    employees = get_file_data("database/employees.json")
    for i in range(len(employees)):
        print(f'{i}: ')
        print(f'\t{employees[i]["email"]}')
        print(f'\t{employees[i]["first_name"]}')
        print(f'\t{employees[i]["last_name"]}')
        print(f'\t{employees[i]["phone"]}')


def get_employee_by_email(email):
    employees = get_file_data("database/employees.json")
    for employee in employees:
        if employee["email"] == email:
            print(employee["email"])
            print(employee["first_name"])
            print(employee["last_name"])
            print(employee["phone"])


def update_employee_by_id(id, email, first_name, last_name, phone):
    path = "database/employees.json"
    employees = get_file_data(path)
    employees[int(id)] = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone
    }
    save_all(employees, path)


def save_plant(name, address):
    new_plant = {
        "name": name,
        "address": address
    }
    save_to_file(new_plant, "database/plants.json")


def get_all_plants():
    plants = get_file_data("database/plants.json")
    for i in range(len(plants)):
        print(f'{i}: ')
        print(f'\t{plants[i]["name"]}')
        print(f'\t{plants[i]["address"]}')


def get_plant_by_id(id):
    plants = get_file_data("database/plants.json")
    try:
        plant = plants[id]
        print(f"{plant['name']}: {plant['address']}")
    except IndexError:
        print("Plant not found")


def save_salon(name, address):
    salon = {
        "name": name,
        "address": address
    }
    save_to_file(salon, "database/salons.json")


def delete_employee(id):
    employees = get_file_data("database/employees.json")
    try:
        del employees[int(id)]
        save_all(employees, "database/employees.json")
    except Exception:
        pass


def add_sale_dep(name):
    new_dep = {
        "name": name
    }
    save_to_file(new_dep, "database/sale_deps.json")
