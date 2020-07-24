class BankCorp:
    __count_bank_corps = 0

    def __init__(self, name, address, postcode, city):
        self.name = name.capitalize()
        self.address = address
        self.postcode = postcode
        self.city = city
        self.entries = self.__add_bank()
        BankCorp.__count_bank_corps += 1

    def __str__(self) -> str:
        return f"{self.entries}"

    def __repr__(self) -> str:
        return self.__str__()

    def show_name(self) -> str:
        return self.name

    def __add_bank(self):
        return {
            "Name": self.name,
            "Address": self.address,
            "Postcode": self.postcode,
            "City": self.city
        }
