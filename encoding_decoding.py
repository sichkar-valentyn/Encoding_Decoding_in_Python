# File: Encoding_Decoding_in_Python.py
# Description: Simple example how to encode and decode strings in Python
# Environment: PyCharm and Anaconda environment
#
# MIT License
# Copyright (c) 2018 Valentyn N Sichkar
# github.com/sichkar-valentyn
#
# Reference to:
# [1] Valentyn N Sichkar. Simple example how to encode and decode strings in Python // GitHub platform [Electronic resource]. URL: https://github.com/sichkar-valentyn/Encoding_Decoding_in_Python (date of access: XX.XX.XXXX)


# Method encode() returns an encoded version of the string
initial_string = 'Hello there!'
encoded_string = initial_string.encode('utf-32')

# To choose the right Codec for needed language go to the page:
# docs.python.org/3.7/library/codecs.html
# Or choose 'ut-32' as standard for all languages

print('Encoded string of "', initial_string, '" is: ')
print(encoded_string)

# To decode string we need to use decode function
decoded_string = b'\xff\xfe\x00\x00H\x00\x00\x00e\x00\x00\x00l\x00\x00\x00l\x00\x00\x00o\x00\x00\x00 \x00\x00\x00t\x00\x00\x00h\x00\x00\x00e\x00\x00\x00r\x00\x00\x00e\x00\x00\x00!\x00\x00\x00'.decode('utf-32')
print(decoded_string)

# It is possile to use "Fill paragraph" option to show long string in the screen
decoded_string = b'\xff\xfe\x00\x00H\x00\x00\x00e\x00\x00\x00l\x00\x00\x00l\x00\x00\x00o\x00\x00\x00 ' \
                 b'\x00\x00\x00t\x00\x00\x00h\x00\x00\x00e\x00\x00\x00r\x00\x00\x00e\x00\x00\x00!\x00\x00\x00' \
                 b''.decode('utf-32')
print(decoded_string)
