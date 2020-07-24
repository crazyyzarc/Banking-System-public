import datetime
import os


class Logger:
    def __init__(self, name):
        self.name = name
        self.tags = ["INFO", "WARNING", "ERROR"]
        self.root_log = os.path.join(os.getcwd(), "logs/")

    def do_log(self, message: str, code_file: str, code_func: str, tag: str):
        """
        Message:
        Nachricht, die gespeichert wird

        Tags:
        info = Standard & Information
        warning = wichtiger Hinweis
        error = kritischer Fehler
        """
        timestamp = datetime.datetime.now()
        timestamp = timestamp.strftime("%Y-%m-%d")
        tag = tag.upper()

        is_logging = True
        while is_logging:
            try:
                if tag in self.tags:
                    with open(self.root_log + self.name, "a") as file:
                        file.write(f"[{tag}][{timestamp}] {message} in {code_file} ~ {code_func}\n")
                        print(f"Datei {self.name} modifiziert")

                    is_logging = False
                    break
                else:
                    print(f"\n|> Aktion nicht bekannt. Nutze {self.tags[0]}-Tag..")
                    tag = self.tags[0]
                    continue
            except FileNotFoundError:
                try:
                    os.mkdir(self.root_log)
                except FileExistsError:
                    pass

    def read_log(self):
        file_list = []

        try:
            with os.scandir("./logs/") as entries:
                for entry in entries:
                    file_list.append(entry.name)
        except FileNotFoundError:
            try:
                os.mkdir(self.root_log)
            except FileExistsError:
                pass
        if len(file_list) == 0:
            print("\n\tKeine log Dateien vorhanden\n")
            return 0
        try:
            which_file = input(f"Welche Datei möchtest du lesen {file_list}:> ")
            print("")

            with open("./logs/" + which_file, "r") as file:
                for line in file:
                    print("\t", line, end="")

        except FileNotFoundError:
            print("Die Datei exisitert nicht")

    def log_to_csv(self):
        pass

    def log_to_sql(self):
        pass
