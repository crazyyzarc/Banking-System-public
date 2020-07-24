from bank_site.bank_corps import BankCorp
from bank_site.bankaccount import Bankaccount
from client_site import customer
from bank_site import bankaccount
from bank_site import bank_corps
from client_site.customer import Customer
from exception import *


class CliInstances:
    def __init__(self):
        self.client = customer.Customer
        self.bank = bankaccount.Bankaccount
        self.bank_corp = bank_corps.BankCorp
        self.customer_details = None
        self.bank_details = None
        self.bank_account_details = None
        self.commands = {"customer", "bank", "bankaccount"}
        self.cli_sign_name = None
        self.cli_sign_bank = None

    def session_logon(self, session_password) -> bool:
        if isinstance(self.customer_details, customer.Customer):
            return self.customer_details.session_logon(session_password)
        else:
            return False

    def get_create(self, command: str):
        is_creating = True
        command.lower()

        while is_creating:
            try:
                # print("I've been here in get_create (cli.py)")
                if command == "customer":
                    # firstname = input("Vorname:> ")
                    # lastname = input("Nachname:> ")
                    # gender = input("Geschlecht [m/w]:> ")
                    # birth = input("Geburtsdatum:> ")
                    # address = input("Adresse:> ")
                    # postcode = input("Postleitzahl:> ")
                    # city = input("Stadt:> ")
                    self.customer_details = self.client(firstname="Max", lastname="Mustermann",
                                                        gender="m", birth="19.04.1995",
                                                        address="Postweg 5", postcode="53111", city="Bonn")
                    self.cli_sign_name = "Meier".upper()
                    return self.customer_details

                elif command == "bank":
                    # bank_name = input("Name der Bank:> ")
                    # bank_address = input("Addresse der Bank:> ")
                    # bank_postcode = input("Postleitzahl der Bank:> ")
                    # bank_city = input("Ort der Bank:> ")
                    self.bank_details = self.bank_corp(name="dkb", address="Der heiße Weg 2", postcode="53235", city="bonn")
                    return self.bank_details

                elif command == "bankaccount":
                    if self.customer_details and self.bank_details:
                        # bank = input("Bank:> ").capitalize()
                        bank = "Dkb"

                        if bank in self.bank_details.name:
                            # balance = input("Guthaben:> ")
                            self.bank_account_details = self.bank(customer_details=self.customer_details,
                                                                  bank_name=self.bank_details,
                                                                  balance=4000)
                            self.cli_sign_bank = f"Dkb".upper()
                            return self.bank_account_details
                        else:
                            print("\n|> Bank exisitert nicht!\n")

                    elif self.customer_details is None:
                        print("\n|> Es exisitert noch kein Kunde\n")
                    elif self.bank_details is None:
                        print("\n|> Es exisitert noch keine Bank\n")
                    else:
                        print("\n|> Unerwarteter Fehler\n")

                    return self.bank_account_details

                else:
                    print("\n|> Befehl gibt es nicht!\n")
                    return False

            except ValueError:
                raise ValueError

    def get_help(self, help_commands: dict):
        print("\nCommands:")
        for key in help_commands.keys():
            print("-", key, "", end="")
            if key == "create":
                print("<customer[/bank[/bankaccount]]>")
            elif key == "show":
                print("<customer[/bank[/bankaccount]]>")
            elif key == "withdraw":
                print("<amount> <pin>")
            elif key == "transfer":
                print("<amount> <recipient> <pin>")
            elif key == "deposit":
                print("<amount>")
            else:
                print("")
        else:
            print("")

    def get_show(self, command):
        if command == "customer" and self.customer_details is not None:
            if isinstance(self.customer_details, Customer):
                print(self.customer_details)
        elif command == "bank" and self.bank_details is not None:
            if isinstance(self.bank_details, BankCorp):
                print(self.bank_details)
        elif command == "bankaccount" and self.bank_account_details is not None:
            if isinstance(self.bank_account_details, Bankaccount):
                print(self.bank_account_details)
        elif command == "balance" and self.bank_account_details is not None:
            if isinstance(self.bank_account_details, Bankaccount):
                self.bank_account_details.show_amount()
        else:
            print(f"\n|> {command!r} gibt es nicht!\n")

    def do_withdraw(self, amount, pin):
        if self.bank_account_details is not None and isinstance(self.bank_account_details, Bankaccount):
            self.bank_account_details.withdraw(amount, pin)
        else:
            print("\n|> Es existiert noch kein Konto!\n")

    def do_transfer(self, recipient, amount, pin):
        if self.bank_account_details is not None and isinstance(self.bank_account_details, Bankaccount):
            self.bank_account_details.transfer_to(recipient, amount, pin)
        else:
            print("\n|> Es existiert noch kein Konto!\n")

    def do_deposit(self, amount):
        if self.bank_account_details is not None and isinstance(self.bank_account_details, Bankaccount):
            self.bank_account_details.deposit(amount)
        else:
            print("\n|> Es existiert noch kein Konto!\n")



