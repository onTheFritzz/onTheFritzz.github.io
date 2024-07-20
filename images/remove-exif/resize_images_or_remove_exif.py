from PIL import Image
from math import ceil
import os

def resizeImage():
	imageFile = 'easypeasy.jpg'
	reduceBy = 3

	image = Image.open(imageFile)
	print(f"Original size: {image.size}") # 5464x3640

	length, width = image.size[0], image.size[1]
	length, width = ceil(length/reduceBy), ceil(width/reduceBy)
	blogSize = (length, width)

	print(f'Resized: {length}, {width}')

	resizeImage = image.resize(blogSize)

	imageName = imageFile.split('.')[0]
	outputName = f'{imageName}_{length}-{width}.jpg'
	resizeImage.save(outputName)

def removeExif():
	removeExif = []
	for root, dirs, files in os.walk('.'):
		for file in files:
			print(file)
			if file.split('.')[-1].lower() not in ['jpg', 'png', 'gif']:
				pass
			else:
				print(f'Removed EXIF from: {file}')
				removeExif.append(file)

	for each in removeExif:
		image = Image.open(each)

		# next 3 lines strip exif
		data = list(image.getdata())
		image_without_exif = Image.new(image.mode, image.size)
		image_without_exif.putdata(data)

		image_without_exif.save(each)
	
#resizeImage()
removeExif()