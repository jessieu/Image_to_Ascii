"""
Written by Weilan Yu
This program converts image to ascii.
Reference = "https://www.jianshu.com/p/716c1bda0a98"
"""

import argparse
from PIL import Image

#argumentparser object
parse = argparse.ArgumentParser()

#source file to be converted
parse.add_argument('src')
#take one argument, output filename
parse.add_argument('-o', "--output")
#ouput width
parse.add_argument("--width", type = int, default = 80)
#output height
parse.add_argument("--height", type = int, default = 80)
#get user input arguments
args = parse.parse_args()

#store arguments
IMG = args.src
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

#charcter list for converter reference
char_lst = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/""\\|()1{ }[]?-_+~<>i!lI;:,\"^`'.")
lst_len = len(char_lst)

#black=0, white=255
#red, green, blue
def char_converter(r,g,b,alpha=256):
	if alpha == 0:
		return ' '
	#convert each pixel to gray scale(0-255) 
	gray = 0.2126 * r + 0.7152 * g + 0.0722 * b	

	#the number of unit shared the same character
	unit = (256.0 + 1) / lst_len
	return char_lst[int(gray/unit)]

if __name__ == '__main__':	
	img = Image.open(IMG)
	"""
	Image.resize(size, resample=0)
	size is a tuple (w,h)
	Image.nearest uses nearest neighbour
	"""
	img = img.resize((WIDTH,HEIGHT), Image.NEAREST)

	txt = " "

	for h in range(HEIGHT):
		for w in range(WIDTH):
			#*collect all positional arguments in a tuple
			txt += char_converter(*img.getpixel((w,h)))
		txt += '\n'	
	print(txt)		

	#write to output
	if OUTPUT:
		with open(OUTPUT,'w') as f:
			f.write(txt)
	else:
		with open('output.txt', 'w') as f:
			f.write(txt)		



