class ImageFilter(object):

  def __init__(self, image, filter_name):
    self.image = image
    self.filter_name = filter_name

    self.filters = {
      'grayscale': self.__grayscale,
      'luminance': self.__luminance,
      'desaturation': self.__desaturation,
      'min_decomposition': self.__min_decomposition,
      'max_decomposition': self.__max_decomposition
    }

    self.filter = self.filters[filter_name]

  def applyFilter(self):
    image_pixels = self.image.load()

    width, height = self.image.size

    for x in range(width):
      for y in range(height):
        pixel = image_pixels[x,y]
        filtered_pixel_value = self.filter(pixel)
        image_pixels[x,y] = tuple([filtered_pixel_value] * 3)

  def saveImage(self):
    image_name, image_format = self.image.filename.split('.')
    self.image.save("%s-after-%s.%s" % (image_name, self.filter_name, image_format))

  def __grayscale(self, pixel):
    return int(sum(pixel) / 3)

  def __luminance(self, pixel):
    return int(pixel[0] * 0.3) + int(pixel[1] * 0.59) + int(pixel[2] * 0.11)

  def __desaturation(self, pixel):
    return int(max(pixel) + min(pixel) / 2)

  def __min_decomposition(self, pixel):
    return min(pixel)

  def __max_decomposition(self, pixel):
    return max(pixel)

