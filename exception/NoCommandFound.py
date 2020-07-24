class NoCommandFound(Exception):
    """
    Triggert, wenn der eingebene Befehl nicht exisitert
    Caller: CLI
    """
    def __init__(self, command):
        self.command = command

    def __str__(self):
        details = f"\n|> Keine Option für {self.command!r} vorhanden!\n"
        return details
