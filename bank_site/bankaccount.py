from client_site import customer
from backend import logging as log
from exception import NoAccountException as ex
from random import randint as rint
from bank_site import bank_corps


class Bankaccount:
    """Bankaccount Verwaltung"""
    count_bank_accounts = 0

    def __init__(self, customer_details, bank_name, balance=0.0):
        Bankaccount.count_bank_accounts += 1
        if isinstance(customer_details, customer.Customer):
            self.__customer = customer_details
        else:
            self.__customer = None
        self.bank_name: str = bank_name
        self.__balance: float = balance
        self.max_daily_transfer: int = 5_000
        self.max_transfer: int = 10_000
        self.__iban: str = f"DE{rint(10_000_000_000_000_000_000, 99_999_999_999_999_999_999)}"
        # self.__pin: int = rint(1_000, 9_999)
        self.__pin: int = 4444
        # for non-cli debug -> self.__pin = "4444"
        self._bank_account = self.__add_account(customer_details, bank_name, balance,
                                                max_daily_transfer=500, max_transfer=10_000)
        self.logger = log.Logger("bankaccount.log")
        print(f"\nHallo {self.__customer.firstname} {self.__customer.lastname}")
        print(f"Deine PIN lautet: {self.__pin}")
        print(f"Deine IBAN lautet: {self.__iban}")
        print(f"Die Bank bedankt sich für Ihr Vertrauen in uns!")
        print("-" * 10)

    def __str__(self) -> str:
        return f"{self._bank_account}"

    def __repr__(self) -> str:
        return self.__str__()

    def __len__(self) -> int:
        return len(self._bank_account)

    def add_balance(self, amount) -> float:
        self.__balance += amount
        return self.__balance

    def __lookup_name(self):
        return self.__customer.firstname, self.__customer.lastname

    def __add_account(self, customer_details, bank_name, balance, max_daily_transfer, max_transfer):
        return {
            "Customer": customer_details,
            "Bank name": bank_name,
            "Balance": balance,
            "Max daily transfer": max_daily_transfer,
            "Max transfer": max_transfer
        }

    def withdraw(self, amount: float, pin: int, transfer=False, _recipient=None):
        """
        Geld Auszahlung
        Parameter: <amount> <pin>
        """
        try:
            amount = float(amount)
            pin = int(pin)
            if transfer is False and self.__pin == pin:
                if (float(self.__balance) > 0 and float(self.__balance) > amount and
                        amount < self.max_daily_transfer and amount < self.max_transfer):
                    self.__balance -= amount
                    self.max_daily_transfer += amount
                    print(f"Erfolgreich {amount} EUR ausgezahlt!")
            elif transfer is False and self.__pin != pin:
                print("Die PIN ist inkorrekt")
                self.logger.do_log("Die PIN ist inkorrekt", "bankaccount.py", "withdraw", "warning")
            elif (transfer is True and isinstance(_recipient, Bankaccount) and
                  self.__pin == pin and _recipient.__customer is not None):
                if (self.__balance > 0 and self.__balance > amount
                        and amount < self.max_daily_transfer):
                    self.__balance -= amount
                    self.max_daily_transfer += amount
                    _recipient.add_balance(amount)
                    print(f"Erfolgreich {amount} EUR an {_recipient.__lookup_name()} versendet!")
            elif (transfer is True and isinstance(_recipient, Bankaccount) and self.__pin != pin and
                    _recipient.__customer is not None):
                print("Die PIN ist inkorrekt")
                self.logger.do_log("Die PIN ist inkorrekt", "bankaccount.py", "withdraw", "warning")
            else:
                print("Etwas ist schief gelaufen. Siehe log Datei")
                if not isinstance(_recipient, Bankaccount):
                    self.logger.do_log(f"Das benutzte Bankkonto '{_recipient}' ist kein Bankkonto",
                                       "bankaccount.py", "withdraw", "error")
                elif _recipient.__customer is None:
                    self.logger.do_log("Das dahinter befindliche Customer Objekt ist kein Customer Objekt",
                                       "bankaccount.py", "withdraw", "error")
                elif self.__pin != pin:
                    self.logger.do_log("Die PIN ist inkorrekt", "bankaccount.py", "withdraw", "warning")
                else:
                    self.logger.do_log(f"Ein noch unbekannter Fehler ist aufgetreten",
                                       "bankaccount.py", "withdraw", "error")
                raise ex.NoAccountException(self.__lookup_name(), _recipient, amount)

        except AttributeError:
            print("\n|> Das Konto existiert nicht!\n")
            self.logger.do_log("Konto ist nicht existent!", "bankaccount.py", "withdraw", "warning")
        except ValueError:
            print("\n|> Falscher Datentyp!\n")
            self.logger.do_log("Es wurde keine Zahl eingegeben", "bankaccount.py", "withdraw", "error")

    def show_amount(self):
        """
        Finanzübersicht
        """
        if self.__customer is None:
            print("\n|> Kontozugriff verwert!\n")
            self.logger.do_log("Das Konto ist nicht existent", "bankaccount.py", "show_amount", "error")
        else:
            print(f"Hallo {' '.join(self.__lookup_name())}. Dein Kontostand liegt bei {self.__balance:.2f} EUR!")

    def deposit(self, amount: float):
        """
        Geld Einzahlung
        Parameter <amount>
        """
        amount = float(amount)
        self.__balance += amount
        print(f"Erfolgreich {amount} eingezahlt!")

    def transfer_to(self, recipient, amount: float, pin):
        """
        Überweisung von Kunde A nach Kunde B
        Parameter: <recipient> <amount> <pin>
        """
        # if isinstance(recipient, self.__customer):
        #     print("Wie schön, dass du dir selbst Geld schenkst ;-)")
        self.withdraw(amount, pin, transfer=True, _recipient=recipient)
