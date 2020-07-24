class NoAccountException(Exception):
    """
    Triggert, wenn kein Account existiert
    Caller: banking & bankaccount handler
    """
    def __init__(self, sender, recipient, value):
        self.sender = sender
        self.recipient = recipient
        self.value = value

    def __str__(self):
        details = "\n|> Fehler bei der Transaktion:\n"
        details += f"|> Begünstiger: {self.sender}\n"
        details += f"|> Empfänger: {self.recipient}\n"
        return details
