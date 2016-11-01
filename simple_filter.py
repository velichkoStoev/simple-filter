import  argparse
from PIL import Image
from image_filter import ImageFilter

if __name__ == '__main__':
  available_filters = ['grayscale', 'luminance', 'desaturation', 'min_decomposition', 'max_decomposition']

  parser = argparse.ArgumentParser(description="Providing a basic functionality for filtering an image")
  parser.add_argument('-p', '--path', required=True, help="The path to the image file", metavar='')
  parser.add_argument('-f', '--filter', required=True, help="The name of the filter. Available filters: " + ', '.join(available_filters), metavar='', choices=available_filters)
  args = parser.parse_args()

  print("Loading image (%s) ..." % args.path)
  image = Image.open(args.path)
  print("Image loaded")

  image_filter = ImageFilter(image, args.filter)

  print("Applying filter (%s)..." % args.filter)
  image_filter.applyFilter()
  print("Filter applied.")

  print("Saving the new image ...")
  image_filter.saveImage()
  print("Image saved.")