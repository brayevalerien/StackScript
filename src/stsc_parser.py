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
    
    def register_tags(self) -> dict:
        if self.tokens == None:
            raise RuntimeError("Cannot register tag before parsing.")
        self.tags = {}
        for ip, token in enumerate(self.tokens):
            if token[0] == ">": # found a tag
                self.tags[token[1:]] = ip
        return self.tags