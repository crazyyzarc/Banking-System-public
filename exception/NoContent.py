class NoContent(Exception):
    """
    Triggert, wenn das ausgewählte Objekt kein Inhalt enthält
    Caller: CLI
    """
    def __init__(self, command):
        self.command = command

    def __str__(self):
        details = f"\n|> Kein Eintrag für {self.command!r} gefunden!\n"
        return details
