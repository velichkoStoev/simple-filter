from PIL import Image

def grayscale_filter(pixel):
  red, green, blue = pixel

  gray = int((red + green + blue) / 3)

  return (gray, gray, gray)

def luminance_filter(pixel):
  red, green, blue = pixel

  gray = (int(red * 0.3) + int(green * 0.59) + int(blue * 0.11))

  return (gray, gray, gray)

def desaturation_filter(pixel):
  red, green, blue = pixel

  gray = int((max(red, green, blue) + min(red, green, blue)) / 2)

  return (gray, gray, gray)

def min_decomposition_filter(pixel):
  red, green, blue = pixel

  gray = min(red, green, blue)

  return (gray, gray, gray)

def max_decomposition_filter(pixel):
  red, green, blue = pixel

  gray = max(red, green, blue)

  return (gray, gray, gray)

if __name__ == '__main__':
  filename = 'test.jpg'

  image = Image.open(filename)
  image_pixels = image.load()

  width, height = image.size

  for x in range(width):
    for y in range(height):
      image_pixels[x,y] = max_decomposition_filter(image_pixels[x,y])

  image.save('max-decomposition-image.jpg')

  del image