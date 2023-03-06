# There is an encoded string using Morse code. The codes are separated by a space.
# It is necessary to decode it using the Morse code from the previous lesson.
# The received message (string) is displayed on the screen.

morse = {')': '-.--.-', '(': '-.--.-', ',': '.-.-.-', '?': '..--..', '!': '--..--', ':': '---...', '.': '......',
         ' ': '-...-', 'A': '.-', 'B': '-...', 'W': '.--', 'G': '--.', 'D': '-..', 'E': '.', 'V': '...-', 'Z': '--..',
         'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'R': '.-.',
         'S': '...', 'T': '-', 'U': '..-', 'F': '..-.', 'H': '....', 'C': '-.-.', 'Q': '--.-', 'Y': '-..-', 'X': '-.--'
         }

string = '--. --- --- -.. -...- .-.. ..- -.-. -.- -...- .- -. -.. -...- .... .- ...- . -...- .- -...- -. .. -.-. . ' \
         '-...- -.. .- -..-'.split()
new_string = []
for l in string:
    for key, vol in morse.items():
        if vol == l:
            new_string.append(key.lower())
            break
print(*new_string, sep='')
