from PIL import Image, ImageFont, ImageDraw

class Code:
	
	length = None		# length of the code in digits
	position = None		# X position to start rendering, in pixels
	
	# digit encodings
	L = {0 : "0001101", 1 : "0011001", 2 : "0010011", 3 : "0111101", 4 : "0100011", 
		5 : "0110001", 6 : "0101111", 7 : "0111011", 8 : "0110111", 9 : "0001011"}
	
	R = {0 : "1110010", 1 : "1100110", 2 : "1101100", 3 : "1000010", 4 : "1011100",
		5 : "1001110", 6 : "1010000", 7 : "1000100", 8 : "1001000", 9 : "1110100"}
	
	def __init__(self, codeStr):
		assert len(codeStr) == self.length
		self.codeStr = codeStr
		self.codeNum = [int(x) for x in codeStr]
		self.calcCode()

	def calcCode(self):
		''' Method converting the code to 'bit' sequence (0/1/L)
		- to be overriden in subclasses'''
		raise NotImplementedError()
		
	def calcChecksum(self):
		'''Checksum calculation - to be overriden'''
		raise NotImplementedError()
		
	def verifyChecksum(self):
		return self.codeNum[self.length-1] == self.calcChecksum()
		
	def drawText(self, draw, height):
		'''Draw the numbers - to be overriden'''
		raise NotImplementedError()
		
	def drawImage(self, height = 30, extension = "PNG", path=''):
		'''Draw the code
		@param height: height of the image in pixels
		@param extension: extension of the image file
		@param path: path to the image will be path/code.extension'''

		# Create a new image
		im = Image.new("1", (len(self.code) + self.position, height))

		# Create drawer
		draw = ImageDraw.Draw(im)

		# Erase image
		draw.rectangle(((0,0), (im.size[0],im.size[1])), fill=256)
		
		self.drawText(draw, height)

		# Draw the bar codes
		for bit in range(len(self.code)):
			# Draw normal bar
			if self.code[bit] == '1':
				draw.rectangle(((bit + self.position, 0), (bit + self.position, height-10)), fill=0)
			# Draw long bar
			elif self.code[bit] == 'L':
				draw.rectangle(((bit + self.position, 0), (bit + self.position, height-3)), fill=0)

		# Save the result image
		im.save(path + self.codeStr + "." + extension.lower(), extension.upper())
		