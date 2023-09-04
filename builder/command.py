class Command:
    def __init__(self) -> None:
        self.parts = []

    def add(self, data: str) -> None:
        self.parts.append(data)

    def prepare_command(self) -> str:
        return ' '.join(self.parts)
