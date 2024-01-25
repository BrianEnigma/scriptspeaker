#!/usr/bin/env python3
import os
import shlex

from script import Line, Script
from typing import Dict, List

USABLE_VOICES:List[str] = [
    'Agnes',
    'Alex',
    'Allison',
    'Ava',
    'Daniel',
    'Evan',
    'Joelle',
    'Karen',
    'Nathan',
    'Nicky',
    'Noelle',
    'Samantha',
    'Susan',
    'Tom',
    'Zoe',
    'Karen',
    'Lee',
    'Matilda',
    'Isha',
    'Rishi',
    'Sangeeta',
    'Veena',
    'Moira',
    'Fiona',
    'Tessa',
    'Daniel',
    'Jamie',
    'Kate',
    'Oliver',
    'Serena',
    'Stephanie'
]

class AudioGenerator:
    def __init__(self, script:Script, voice_mapping:Dict[str, str]):
        self._script:Script = script
        self._character_voice_mapping:Dict[str, str] = voice_mapping
        self._file_counter = 0
        voice_counter = 0
        os.system('rm -rf ./tmp')
        os.system('mkdir -p ./tmp')
        for character in self._script.characters:
            if character not in self._character_voice_mapping:
                self._character_voice_mapping[character] = USABLE_VOICES[voice_counter]
                voice_counter += 1

    def generate(self, outfile:str):
        with open('./tmp/input.txt', 'w') as f:
            for line in self._script.lines:
                self._file_counter += 1
                output_filename = './tmp/file{0}.aiff'.format(self._file_counter)
                command = "say -v '{0}' -o '{1}' {2}".format(
                    self._character_voice_mapping[line.character],
                    output_filename,
                    shlex.quote(line.line)
                    )
                print(command)
                os.system(command)
                f.write("file '{0}'\n".format(os.path.basename(output_filename)))
                if self._file_counter == 10:
                    break
        os.system('cd tmp ; ffmpeg -f concat -i input.txt -y "../{0}"'.format(outfile))
        os.system('cd tmp ; ffmpeg -f concat -i input.txt -vn -filter:a "atempo=1.25" -y "../fast-{0}"'.format(outfile))
