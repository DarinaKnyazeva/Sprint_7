import datetime
import random
import string


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def generate_random_num():
    string_of_digits = ''
    for i in range(10):
        string_of_digits += str(i)
    return string_of_digits


def register_new_courier_and_return_login_password():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload


def register_new_order():
    firstName = generate_random_string(10)
    lastName = generate_random_string(10)
    address = generate_random_string(10)
    metroStation = "Царицино"
    phone = generate_random_num()
    rentTime = random.randint(1, 9)
    deliveryDate = datetime.date(2025, 7, 1)
    comment = generate_random_string(10)
    color = []

    payload = {
        "firstName": firstName,
        "lastName": lastName,
        "address": address,
        "metroStation": metroStation,
        "phone": phone,
        "rentTime": rentTime,
        "deliveryDate": deliveryDate,
        "comment": comment,
        "color": color
    }

    return payload
