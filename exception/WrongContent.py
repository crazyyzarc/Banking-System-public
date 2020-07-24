class WrongContent(Exception):
    """
    Triggert, wenn der eingebene Inhalt inkorrekt ist
    Caller: CLI
    """
    def __init__(self, specific):
        self.specific = specific

    def __str__(self):
        details = f"Falsche {self.specific} Angabe"
        return details
