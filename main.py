#goofy ahh message translater and encoder for minecraft

code = {
    'A': 'e',
    'B': 'm',
    'C': 'n',
    'D': 'o',
    'E': 'u',
    'F': 'q',
    'G': 'r',
    'H': 's',
    'I': 'p',
    'J': 't',
    'K': 'v',
    'L': 'w',
    'M': 'x',
    'N': 'y',
    'O': 'g',
    'P': 'a',
    'Q': 'd',
    'R': 'z',
    'S': 'b',
    'T': 'l',
    'U': 'f',
    'V': 'c',
    'W': 'j',
    'X': 'i',
    'Y': 'h',
    'Z': 'k',
    ' ': ' ',
    '0': '@',
    '1': ')',
    '2': ':',
    '3': '?',
    '4': '=',
    '5': '+',
    '6': '%',
    '7': '/',
    '8': ',',
    '9': '&',
    '&': '.-...',
    "'": '.----.',
    '@': '.--.-.',
    ')': '-.--.-',
    '(': '-.--.',
    '': '---...',
    ',': '--..--',
    '=': '-...-',
    '!': '-.-.--',
    '.': '.-.-.-',
    '-': '-....-',
    '+': '.-.-.',
    '"': '.-..-.',
    '?': '..--..',
    '/': '-..-.'
}

mode = input("Translate or Encode:\n").lower()
message = input('Enter what you would like to translate/encode:\n')

if mode == "encode":
  for i in range(len(message)):
    print(code[message[i].upper()], end=' ')

if mode == "translate":
  print('The translated message is:\n')
  for i in range(len(message)):
    for key, value in code.items():
      if value == message[i]:
        print(key, end=" ")
