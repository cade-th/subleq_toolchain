import re

token_t = [
    ["number", r'-?\d+'],
    ["hash", r'#'],
    ["label", r'\w+:'],
    ["symbol", r'\w+'],
    ["RPAREN", r'\('],
    ["LPAREN", r'\)'],
    ["whitespace", r'\s+']
]

class Lexer:
    def __init__(self, string):
        self.tokens = []
        self.pos = 0
        self.string = string

    def lex(self):
        
        while self.pos < len(self.string):
            matched = False 
            substring = self.string[self.pos:]

            for token_type, pattern in token_t:
                match = re.match(pattern, substring)
                if match:
                    self.pos+= match.end()
                    matched = True
                    if token_type != 'whitespace':
                        self.tokens.append([token_type, match.group()])
                    break

            if not matched:
                print(f"Unknown character at {self.pos}")

        return self.tokens
