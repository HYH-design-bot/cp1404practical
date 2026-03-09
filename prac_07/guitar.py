class Guitar:
    def __init__(self, name: str, year: int, cost: int):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"({self.name} ({self.year}) : {self.cost})"

    def __repr__(self):
        """Provide developer-friendly representation of a ProgrammingLanguage."""
        return f"{vars(self)}"

    def __lt__(self, other):
        """Provide developer-friendly representation of a ProgrammingLanguage."""
        return True if self.cost < other.cost else False