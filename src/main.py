#!/usr/bin/env python3

from audio_gen import AudioGenerator
from parser import UkScriptParser
from script import Script

parser = UkScriptParser('script.txt', True)
script:Script = parser.parse()
print(script)
mapping = {
    'AMELIA': 'Serena',
    'CASSIE': 'Kate',
    'VAL': 'Zoe'
}
generator = AudioGenerator(script, mapping)
generator.generate('output.mp3')
