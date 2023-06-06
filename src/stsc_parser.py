class Parser:
    def __init__(self) -> None:
        pass

    def parse(self, s: str) -> list[str]:
        self.tokens = []
        for line in s.splitlines():
            if '//' in line: # comment
                line = line[:line.index("//")].strip()
            tokens = line.strip().split()
            self.tokens.extend(tokens)
        return self.tokens