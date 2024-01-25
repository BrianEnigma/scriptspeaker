#/usr/bin/env python3

import re
from script import Script

class Parser:
    def __init__(self, file:str, remove_stage_direction:bool):
        self._file:str = file
        self._remove_stage_direction:bool = remove_stage_direction

    def parse(self) -> Script:
        pass

    def _perform_remove_stage_direction(self, line:str):
        if self._remove_stage_direction:
            # Remove anything within parentheses.
            line = re.sub('\([^)]+\)', '', line)
        return line

    def __str__(self):
        return "Parser"

    def __repr__(self):
        return "Parser"

class UkScriptParser(Parser):
    def __init__(self, file:str, remove_stage_direction:bool):
        super().__init__(file, remove_stage_direction)
        self._line_matcher = re.compile('^([A-Z]+):[ \t]+(.*)$')

    def parse(self) -> Script:
        result:Script = Script()
        with open(self._file, 'r') as f:
            for line in f:
                if line is None or line == '':
                    break
                line = line.strip()
                match = self._line_matcher.match(line)
                if match:
                    result.add_line(
                        match.group(1),
                        self._perform_remove_stage_direction(match.group(2)))
        return result

    def __str__(self):
        return "UKScriptParser"

    def __repr__(self):
        return "UKScriptParser"