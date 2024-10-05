from PIL import Image,ImageFilter

img = Image.open("paisaje.jpg")

img.filter(ImageFilter.CONTOUR).show()
img.filter(ImageFilter.DETAIL).show()
img.filter(ImageFilter.EDGE_ENHANCE).show()
img.filter(ImageFilter.EDGE_ENHANCE_MORE).show()
img.filter(ImageFilter.EMBOSS).show()
img.filter(ImageFilter.FIND_EDGES).show()
img.filter(ImageFilter.SMOOTH).show()
img.filter(ImageFilter.SMOOTH_MORE).show()