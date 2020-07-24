import os
import datetime
import string
import random


class SaveDB:
    def __init__(self, name):
        self.name = name
        self.__token = None
        self.root_log = os.path.join(os.getcwd(), "database/")

    def do_save(self, *params):
        timestamp = datetime.datetime.now()
        timestamp = timestamp.strftime("%Y.%m.%d-%H:%M:%S")
        self.gen_token()

        with open(os.path.join(self.root_log, self.name), "a") as file:
            file.write(f"[{timestamp}~{self.__token}] {params}\n")

    def do_restore(self, token):
        if token is None:
            print("\nToken fehlt\n")
        elif token == self.__token:
            print("TOKEN KORREKT")

    def gen_token(self, length=10):
        abc = string.ascii_letters
        self.__token = "".join(random.choice(abc) for char in range(length))