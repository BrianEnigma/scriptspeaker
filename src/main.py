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
    'VAL': 'Zoe',
    'LAURA': 'Susan',
    'ROBBIE': 'Jamie',
    'CHARLIE': 'Oliver',
    'MAX': 'Kate',
    'LEO': 'Tom',
    'BETH': 'Isha',
    'SARAH': 'Moira',
    'BROCK': 'Lee',
    'JIM': 'Jamie',
    'BART': 'Oliver',
    'TRAVIS': 'Evan',
    'JOURNALIST': 'Ava'
}
generator = AudioGenerator(script, mapping)
generator.generate('output.mp3')
