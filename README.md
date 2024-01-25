placeholder


Parser rules:

- Anything that is a line consisting of UPPERCASE, a colon, some whitespace, and text is considered a line to read.
- Anything else (a line starting in UPPERCASE without a colon, a parenthetical line, etc) is ignored and not considered a spoken line.
- Anything within the spoken line between parentheses is considered inline stage direction. It can be optional stripped out.

Install Prerequisites:

- Running on macOS. We need its `say` command and list of voices.
- `ffmpeg` installed to stitch together audio.
- Install all desired “Enhances” and “Premium” voices.
    - Do this in Settings > Accessibility > Spoken Content > (system voice dropdown) > “Manage Voices...”
    - Click the download button next to any/all “Enhanced” or “Premium” voices you'd like to use.

Running

- Edit the mapping of CHARACTER to voice name in `main.py`
- Put your script in the same directory.
- Run main.py
