"""Kundenbezogene und Anwenderseitige Aktionen"""

from exception import WrongContent as ex


class Customer:
    """Customer Verwaltung"""
    count_customer = 0

    def __init__(self, firstname, lastname, gender, birth, address, postcode, city):
        Customer.count_customer += 1
        self.firstname = firstname.capitalize()
        self.lastname = lastname.capitalize()
        self.gender = gender
        try:
            self.__birth: dict = self.__birth_to_dict(birth)
        except ex.WrongContent:
            raise ex.WrongContent("Geburtstag")
        self.__session_token = "1414"
        self.__address = address.title()
        self.__postcode = postcode
        self.__city = city.title()
        self.__entries = self.__add_customer(self.firstname, self.lastname, self.gender, self.__birth,
                                             self.__address, self.__postcode, self.__city)

    def __str__(self) -> str:
        return f"{self.__entries}"

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self) -> int:
        return len(self.__entries)

    def __birth_to_dict(self, birth: str) -> dict:
        try:
            birth_list = birth.split(".")
            birth_dict = {
                "Day": birth_list[0],
                "Month": birth_list[1],
                "Year": birth_list[2]
            }
            del birth_list
            return birth_dict
        except IndexError:
            raise ex.WrongContent("Geburtstag")

    def session_logon(self, session_password) -> bool:
        if session_password == self.__session_token:
            return True
        else:
            return False

    def _slice_address(self, address: str) -> dict:
        address_dict = {
            "Street": "".join([char if char.isalpha() else " " for char in address]).strip(),
            "Number": "".join([char for char in address if char.isdigit()])
        }

        return address_dict

    def __add_customer(self, firstname, lastname, gender, birth, address, postcode, city):
        return {
            "Firstname": firstname,
            "Lastname": lastname,
            "Gender": gender,
            "Birth": birth,
            "Address": address,
            "Postcode": postcode,
            "City": city
        }
