import json
from .exceptions import RedArrowWrongEmailException
from .exceptions import RedArrowInvalidPhoneException
from .exceptions import RedArrowInvalidUserIdException


def get_file_data(path):
    file = open(path, "r")
    data_list = json.loads(file.read())
    file.close()
    return data_list


def save_to_file(data: dict, path):
    data_list = get_file_data()
    data_list.append(data)
    file = open(path, "w")
    data_in_json = json.dumps(data_list)
    file.write(data_in_json)
    file.close()


def save_all(data_list, path):
    file = open(path, "w")
    data_in_json = json.dumps(data_list)
    file.write(data_in_json)
    file.close()


def is_valid_user_id(id):
    data_list = get_file_data()
    try:
        data_list[int(id)]
    except IndexError:
        raise RedArrowInvalidUserIdException("Invalid user ID")

    return id


def is_email_valid(email):
    if "@" in email:
        if "." in email.split("@")[1]:
            return email
        else:
            raise RedArrowWrongEmailException(
                'Email invalid without dot!!!!'
                )

    raise RedArrowWrongEmailException('Email invalid without @ !!!!')


def is_phone_valid(phone):
    if phone[:4] == '+380' and len(phone) == 13:
        return phone

    raise RedArrowInvalidPhoneException('Wrong phone number')
