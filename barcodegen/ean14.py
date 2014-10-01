from .code import Code
from PIL import Image, ImageFont, ImageDraw

class Ean14(Code):
	
	length = 14		# length of the code - 13 digits
	position = 0	# start rendering 8 pixels from the left border (to leave place for the first digit)
	
	# additional encodings
	enc = { '0': 'nnWWn', '1': 'WnnnW', '2': 'nWnnW', '3': 'WWnnn', '4': 'nnWnW',
	'5': 'WnWnn', '6': 'nWWnn', '7': 'nnnWW', '8': 'WnnWn', '9': 'nWnWn' }

	def calcCode(self):
	
		self.code = '1010'	# starting sequence
		
		for i in range(0, 14, 2):
			d1 = self.codeStr[i]
			d2 = self.codeStr[i+1]
			for j in range(5):
				self.code += '1' if self.enc[d1][j] == 'n' else '11'
				self.code += '0' if self.enc[d2][j] == 'n' else '00'
		
		self.code += '1101' # ending sequence
		
	def calcChecksum(self):
		weight = [3,1] * 6 + [3]
		magic = 10
		sum = 0

		for i in range(13):         # traditional mod 10 checksum
			sum = sum + self.codeNum[i] * weight[i]
			
		z = ( magic - (sum % magic) ) % magic
		
		if z < 0 or z >= magic:
			return None
			
		return z
		
	def drawText(self, draw, height):
		# Load font
		font = ImageFont.load("courB08.pil")
		
		# Draw number
		draw.text((11, height-9), self.codeStr, font=font, fill=0)
