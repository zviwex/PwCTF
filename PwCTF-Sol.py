"""
Author - ZviWex

This is a solution for prequal.pwctf.com Mini-CTF excercise.

NOTE - insert here the ASCII string from prequal.pwctf.com/login.php
in source line 1337
"""

import codecs
import sys

def decode(encoded_string):
	list_of_bin = encoded_string.decode("hex")[2:].split("0b")


	base64string = ""
	for bin_a in  list_of_bin:
		base64string += chr(int(bin_a,2))

	# Reversing the string
	base64string = base64string[::-1]

	decoded_string = codecs.encode(base64string, 'rot_13').decode("base64")

	return decoded_string

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print "Usage: \"<{}> <string from source>".format(argv[0])

	encoded_string = sys.argv[1] 
	
	decoded_string = decode(encoded_string)

	print decoded_string
