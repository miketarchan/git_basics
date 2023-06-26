from helpers import save, get_all_employers, is_email_valid, is_phone_valid
from helpers import is_valid_user_id
from helpers import update_employee_by_id
from helpers import get_employee_by_email, decorators_helpers
from helpers import RedArrorException


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
        4.Update employee""")

        flag = input("Choose menu item: ")
        if flag == "1":
            save(
                InputProcessor('Email: ', is_email_valid).run(),
                InputProcessor('First Name: ').run(),
                InputProcessor("Last Name: ").run(),
                InputProcessor("Phone Number: ", is_phone_valid).run()
            )
        elif flag == "2":
            get_all_employers()
        elif flag == "3":
            email_to_find = InputProcessor('Type email of employee which you want to find: ', is_email_valid).run()
            get_employee_by_email(email_to_find)
        elif flag == '4':
            update_employee_by_id(
                InputProcessor('Enter user\s ID: ', is_valid_user_id).run(),
                InputProcessor('Email: ', is_email_valid).run(),
                InputProcessor('First Name: ').run(),
                InputProcessor("Last Name: ").run(),
                InputProcessor("Phone Number: ", is_phone_valid).run()
            )


if __name__ == '__main__':
    # InputProcessor('Email: ', is_email_valid)

    run_loop()
