# A string is entered. It is necessary to encode it in Morse code, where each letter is assigned a code from a dot and
# a dash. Each encoded letter must be followed by a space (the letter code ending character).
# There should not be a space after the last code (at the end of the line).

morse = {')': '-.--.-', '(': '-.--.-', ',': '.-.-.-', '?': '..--..', '!': '--..--', ':': '---...', '.': '......',
         ' ': '-...-', 'A': '.-', 'B': '-...', 'W': '.--', 'G': '--.', 'D': '-..', 'E': '.', 'V': '...-', 'Z': '--..',
         'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'F': '..-.', 'H': '....', 'C': '-.-.', 'Q': '--.-', 'Y': '-..-', 'X': '-.--'
         }

string = input('write something: ').upper()
new_string = []
for letter in string:
    new_string.append(morse[letter])
print(*new_string)
