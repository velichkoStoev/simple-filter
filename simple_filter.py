from PIL import Image
from image_filter import ImageFilter

if __name__ == '__main__':
  filename = 'test.jpg'

  image = Image.open(filename)
  image_filter = ImageFilter(image, 'grayscale')
  image_filter.applyFilter()
  image_filter.saveImage()