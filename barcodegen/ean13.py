from .code import Code
from PIL import Image, ImageFont, ImageDraw

class Ean13(Code):
	
	length = 13		# length of the code - 13 digits
	position = 8	# start rendering 8 pixels from the left border (to leave place for the first digit)
	
	# additional encodings
	G = {0 : "0100111", 1 : "0110011", 2 : "0011011", 3 : "0100001", 4 : "0011101",
		5 : "0111001", 6 : "0000101", 7 : "0010001", 8 : "0001001", 9 : "0010111"}

	# encodings depending on the first digit
	family = {0 : (Code.L,Code.L,Code.L,Code.L,Code.L,Code.L), 1 : (Code.L,Code.L,G,Code.L,G,G), 2 : (Code.L,Code.L,G,G,Code.L,G), 
		3 : (Code.L,Code.L,G,G,G,Code.L), 4 : (Code.L,G,Code.L,Code.L,G,G), 5 : (Code.L,G,G,Code.L,Code.L,G), 
		6 : (Code.L,G,G,G,Code.L,Code.L), 7 : (Code.L,G,Code.L,G,Code.L,G), 8 : (Code.L,G,Code.L,G,G,Code.L), 
		9 : (Code.L,G,G,Code.L,G,Code.L)}

	def calcCode(self):
		left = self.family[self.codeNum[0]]
		
		self.code = 'L0L'	# starting sequence
		
		# Compute the left part of bar code
		for i in range(0,6):
			self.code += left[i][self.codeNum[i+1]]
			
		self.code += '0L0L0'	# middle sequence
		
		for i in range (7,13):
			self.code += self.R[self.codeNum[i]]
			
		self.code += 'L0L'	# ending sequence
		
	def calcChecksum(self):
		weight = [1,3] * 6
		magic = 10
		sum = 0

		for i in range(12):         # traditional mod 10 checksum
			sum = sum + self.codeNum[i] * weight[i]
			
		z = ( magic - (sum % magic) ) % magic
		
		if z < 0 or z >= magic:
			return None
			
		return z
		
	def drawText(self, draw, height):
		# Load font
		font = ImageFont.load("courB08.pil")
		
		# Draw first digit
		draw.text((0, height-9), self.codeStr[0], font=font, fill=0)

		# Draw first part of number
		draw.text((self.position + 7, height - 9), self.codeStr[1:7], font=font, fill=0)

		# Draw second part of number
		draw.text((len(self.code)/2 + 6 + self.position, height-9), self.codeStr[7:], font=font, fill=0)
		