from helpers import save_employee, get_all_employers, is_email_valid, \
                    is_phone_valid, is_valid_user_id, update_employee_by_id, \
                    get_employee_by_email, decorators_helpers, \
                    RedArrorException, save_plant, get_all_plants, \
                    get_plant_by_id, save_salon, delete_employee, add_sale_dep


class InputProcessor():

    def __init__(self, input_title, validator=None) -> None:
        self.input_title = input_title
        self.validator = validator

    @decorators_helpers.validata_input
    def __get_user_input_data(self):
        return input(f"{self.input_title}")

    def run(self):
        try:
            input_data = self.__get_user_input_data()
            return input_data
        except RedArrorException as e:
            print(e)
            self.run()


def run_loop():
    while True:
        print("""MENU:
        1.Add new Employee
        2.Get all Employees
        3.Get employee by email
        4.Update employee
        5. Add plant
        6.Get all plants
        7.Get plant by id
        8.Add salon
        9.Delete employee
        10.Add Sale Department""")

        flag = input("Choose menu item: ")
        if flag == "1":
            save_employee(
                InputProcessor('Email: ', is_email_valid).run(),
                InputProcessor('First Name: ').run(),
                InputProcessor("Last Name: ").run(),
                InputProcessor("Phone Number: ", is_phone_valid).run()
            )
        elif flag == "2":
            get_all_employers()
        elif flag == "3":
            email_to_find = InputProcessor(
                'Type email of employee which you want to find: ',
                is_email_valid).run()
            get_employee_by_email(email_to_find)
        elif flag == '4':
            update_employee_by_id(
                InputProcessor('Enter user\'s ID: ', is_valid_user_id).run(),
                InputProcessor('Email: ', is_email_valid).run(),
                InputProcessor('First Name: ').run(),
                InputProcessor("Last Name: ").run(),
                InputProcessor("Phone Number: ", is_phone_valid).run()
            )
        elif flag == 5:
            save_plant(
                InputProcessor('Type a name of Plant: ').run(),
                InputProcessor('Type an address of Plant: ').brun(),
            )
        elif flag == 6:
            get_all_plants()
        elif flag == 7:
            get_plant_by_id(
                 InputProcessor('Id of plant: ').run(),
            )
        elif flag == 8:
            save_salon(
                InputProcessor('Type a name of Salon: ').run(),
                InputProcessor('Type an address of Salon: ').run(),
            )
        elif flag == 9:
            id = int(input("Id of element which you want to delete: "))
            delete_employee(id)
        elif flag == 10:
            add_sale_dep(
                 InputProcessor('Sale department name: ').run()
            )


if __name__ == '__main__':
    # InputProcessor('Email: ', is_email_valid)

    run_loop()
