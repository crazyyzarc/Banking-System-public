"""
Fiktives Banking System
"""
############################
#                          #
#   Projekt: Banking       #
#   Erstellung: 11.06.2020 #
#                          #
############################
# TODO: GENERATE IBAN FROM BIC, BANKCODE AND CHECKSUM
# TODO: ADDING NEW TOOLS THIRD PARTY SCRIPTS
# TODO: ADDING BALANCES IN TXT OR SQL FILES
# TODO: ANALYZE BALANCE WITH MATPLOTLIB
# TODO: ADDING BANK ACCOUNT CREATION SIMULATION
# TODO: ADDRESS WITH SUFFIX LIKE 'Promenaden Weg 5c"
# TODO: WITHDRAW ONLY WITH NOTES LIKE 5€, 10€ and so on

# ADVANCED:
# TODO: MITTEILEN, WENN BENUTZER MEHR ALS SUMME X EINZAHLT IN ZEITRAUM Y UND DIESES WEITER TRANSFERIERT
#  -> UM GELDWÄSCHE ZU VERHINDERN

import exception as ex
from backend import logging
from backend import cli
from bank_site.bank_corps import BankCorp
from bank_site.bankaccount import Bankaccount
from client_site import customer
from bank_site import bankaccount
from bank_site import bank_corps
from client_site.customer import Customer


class Entries:
    kundenbasis = {}
    id = 0
    indexer = {}

    def add_entries(self, retter):
        if isinstance(retter, Customer):
            Entries.id += 1
            Entries.kundenbasis["ID"] = Entries.id
            Entries.indexer[Entries.id] = retter.lastname
            Entries.kundenbasis["Customer"] = retter
        elif isinstance(retter, BankCorp):
            Entries.kundenbasis["BankCorp"] = retter
        elif isinstance(retter, Bankaccount):
            Entries.kundenbasis["Bankaccount"] = retter
        else:
            print("Eintrag nicht hinzugefügt")


    def show_entries(self):
        print(Entries.kundenbasis)
        print(Entries.indexer)


def get_create(cli_object: cli.CliInstances, *params):
    if cli_object is not None:
        if len(params) == 1:
            crm.add_entries(cli_instance.get_create(params[0]))
        else:
            print("\n|> Zu wenige Parameter!\n")
    else:
        print("Instanz ist offline")


def get_show(cli_object: cli.CliInstances, *params):
    if cli_object is not None:
        if len(params) == 1:
            cli_instance.get_show(params[0])
        else:
            print("\n|> Zu wenige Parameter!\n")
    else:
        print("Instanz ist offline")


def get_help(cli_object: cli.CliInstances, *params):
    if cli_object is not None:
        if len(params) == 0:
            cli_instance.get_help(Commands)
        else:
            cli_instance.get_help(Commands)
    else:
        print("Instanz ist offline")


def do_withdraw(cli_object: cli.CliInstances, *params):
    if cli_object is not None:
        if cli_object.bank_account_details is None:
            print("\n|> Es existiert noch kein Konto!\n")
            return -1
        if len(params) == 2:
            cli_instance.do_withdraw(params[0], params[1])
        elif len(params) == 1 and cli_object.bank_account_details is not None:
            print("PIN fehlt")
        else:
            print("\n|> Zu wenige Parameter!\n")
    else:
        print("Instanz ist offline")


def do_transfer(cli_object: cli.CliInstances, *params):
    if cli_object is not None:
        if cli_object.bank_account_details is None:
            print("\n|> Es existiert noch kein Konto!\n")
            return -1
        if len(params) == 3:
            cli_instance.do_transfer(params[0], params[1], params[2])
        elif len(params) == 2 and cli_object.bank_account_details is not None:
            print("PIN fehlt")
        else:
            print("\n|> Zu wenige Parameter!\n")
    else:
        print("Instanz ist offline")


def do_deposit(cli_object: cli.CliInstances, *params):
    if cli_object is not None:
        if cli_object.bank_account_details is None:
            print("\n|> Es existiert noch kein Konto!\n")
            return -1
        if len(params) == 1:
            cli_instance.do_deposit(params[0])
        else:
            print("\n|> Zu wenige Parameter!\n")
    else:
        print("Instanz ist offline")


def do_quit(cli_object: cli.CliInstances, *params):
    raise KeyboardInterrupt


def do_logout(cli_object: cli.CliInstances, *params):
    if cli_object is not None:
        if cli_object.customer_details is None:
            print("\n|> Es existiert noch kein Konto!\n")
            return -1
        if len(params) == 0:
            print("Ausgeloggt..")
            print("\nBenutzerauswahl:")
            for id, name in enumerate(Entries.indexer.values()):
                print(f"({id}) ~ {name}")

        else:
            print("\n|> Zu viele Parameter!\n")
    else:
        print("Instanz ist offline")


Commands = {
    "create": get_create,
    "show": get_show,
    "help": get_help,
    "withdraw": do_withdraw,
    "transfer": do_transfer,
    "deposit": do_deposit,
    "quit": do_quit,
    "logout": do_logout
}


def do_login():
    session_password = input(f"Passwort für [{cli_instance.cli_sign_name}]:> ")
    if cli_instance.session_logon(session_password):
        print(f"Willkommen.. {cli_instance.cli_sign_name}")
        return True
    else:
        print("Passwort ist inkorrekt")
        return False


def intro():
    print(
        r"""
  ____              _    _               ____            _                    ___  _  _   
 | __ )  __ _ _ __ | | _(_)_ __   __ _  / ___| _   _ ___| |_ ___ _ __ ___    / _ \| || |  
 |  _ \ / _` | '_ \| |/ / | '_ \ / _` | \___ \| | | / __| __/ _ \ '_ ` _ \  | | | | || |_ 
 | |_) | (_| | | | |   <| | | | | (_| |  ___) | |_| \__ \ ||  __/ | | | | | | |_| |__   _|
 |____/ \__,_|_| |_|_|\_\_|_| |_|\__, | |____/ \__, |___/\__\___|_| |_| |_|  \___(_) |_|  
                                 |___/         |___/                                      
    """)


def main():
    is_running = True
    # DEBUG MODE
    Commands["create"](cli_instance, "customer")
    Commands["create"](cli_instance, "bank")
    Commands["create"](cli_instance, "bankaccount")
    Commands["withdraw"](cli_instance, "432", "4444")
    Commands["show"](cli_instance, "balance")
    Commands["deposit"](cli_instance, "5323.39")

    # ERROR
    # Commands["transfer"](cli_instance, "reci", "24.99", "4444")
    Commands["show"](cli_instance, "balance")
    Commands["logout"](cli_instance)

    print("\n")

    while is_running:
        try:
            crm.show_entries()
            if len(crm.kundenbasis) == 0:
                print("Noch keine Kundenbasis")
            else:
                pass
                # select_session = int(input("Welchen Kunden möchtest du auswählen?:> "))
                # print("crm.kundenbasis", crm.kundenbasis)
                # print(select_session, type(select_session))
                # if select_session in crm.kundenbasis.values():
                #     print("ist dirn")
                #     print(crm.kundenbasis[select_session])
                # else:
                #     print("not drin")

            if cli_instance.cli_sign_name is not None and cli_instance.cli_sign_bank is None:
                cli_input = input(f"[{cli_instance.cli_sign_name}]:> ").lower().split()
            elif cli_instance.cli_sign_name is not None and cli_instance.cli_sign_bank is not None:
                cli_input = input(f"[{cli_instance.cli_sign_name}~{cli_instance.cli_sign_bank}]:> ").lower().split()
            else:
                cli_input = input(f":> ").lower().split()

            if cli_input[0] in Commands.keys():
                if len(cli_input) == 1:
                    Commands[cli_input[0]](cli_instance)
                elif len(cli_input) == 2:
                    Commands[cli_input[0]](cli_instance, cli_input[1])
                elif len(cli_input) == 3:
                    Commands[cli_input[0]](cli_instance, cli_input[1], cli_input[2])
                else:
                    print("\n|> Zu viele Parameter!\n")

            else:
                print("\n|> Befehl nicht bekannt!\n")

        except ValueError:
            print("\n|> Falscher Datentyp!\n")
            log.do_log("Der Datentyp ist inkorrekt", "banking.py", "main", "error")

        except TypeError:
            print("\n|> Falsche Angabe!\n")
            log.do_log("Benutzung von falschen Datentypen unzulässig", "banking.py", "error")

        except IndexError:
            log.do_log("Zugriff auf eine Liste nicht möglich", "banking.py", "main", "error")
            continue

        except KeyboardInterrupt:
            print("\n..beendet")
            exit(0)


if __name__ == "__main__":
    intro()
    cli_instance = cli.CliInstances()
    crm = Entries()
    log = logging.Logger("banking.log")
    logged_in = 0
    main()
