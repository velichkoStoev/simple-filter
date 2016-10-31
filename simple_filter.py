import  argparse
from PIL import Image
from image_filter import ImageFilter

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description="Providing a basic functionality for filtering an image")
  parser.add_argument('--path', required=True, help="The path to the image file", metavar='')
  parser.add_argument('--filter', required=True, help="The name of the filter", metavar='')
  args = parser.parse_args()

  image = Image.open(args.path)
  image_filter = ImageFilter(image, args.filter)
  image_filter.applyFilter()
  image_filter.saveImage()