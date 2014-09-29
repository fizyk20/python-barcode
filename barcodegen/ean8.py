from .code import Code
from PIL import Image, ImageFont, ImageDraw

class Ean8(Code):
	
	length = 8
	position = 0

	def calcCode(self):
		self.code = 'L0L'	# starting sequence
		
		for i in range(4):
			self.code += self.L[self.codeNum[i]]
			
		self.code += '0L0L0'	# middle sequence
		
		for i in range(4):
			self.code += self.R[self.codeNum[i+4]]
			
		self.code += 'L0L'	# ending sequence
		
	def calcChecksum(self):
		weight = [3,1] * 3 + [3]
		magic = 10
		sum = 0

		for i in range(7):	# traditional mod 10 checksum
			sum = sum + self.codeNum[i] * weight[i]
			
		z = ( magic - (sum % magic) ) % magic
		
		if z < 0 or z >= magic:
			return None
			
		return z
		
	def drawText(self, draw, height):
		# Load font
		font = ImageFont.load("courB08.pil")

		# Draw first part of number
		draw.text((self.position + 7, height - 9), self.codeStr[0:4], font=font, fill=0)

		# Draw second part of number
		draw.text((len(self.code)/2 + 6 + self.position, height-9), self.codeStr[4:], font=font, fill=0)