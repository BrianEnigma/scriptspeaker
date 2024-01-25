#!/usr/bin/env python3
from typing import List

class Line:
    def __init__(self, character:str, line:str, ):
        self.line = line
        self.character = character

    def __str__(self):
        return f"{self.character}: {self.line}\n"

class Script:
    def __init__(self):
        self.characters:set[str] = set()
        self.lines:List[Line] = []

    def add_line(self, character:str, line:str):
        self.characters.add(character)
        self.lines.append(Line(character, line))

    def __str__(self):
        result:str = 'Characters: '
        result += ', '.join(self.characters)
        result += '\n\n'
        for line in self.lines:
            result += str(line)
        return result;
