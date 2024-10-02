from PIL import Image,ImageFilter

imagen = Image.open("paisaje.jpg")

contorno = imagen.filter(ImageFilter.CONTOUR).show()
detalles = imagen.filter(ImageFilter.DETAIL).show()
esquinas = imagen.filter(ImageFilter.EDGE_ENHANCE).show()
esquinas2 = imagen.filter(ImageFilter.EDGE_ENHANCE_MORE).show()
relieve = imagen.filter(ImageFilter.EMBOSS).show()
find = imagen.filter(ImageFilter.FIND_EDGES).show()
suavizado = imagen.filter(ImageFilter.SMOOTH).show()
suavizado2 = imagen.filter(ImageFilter.SMOOTH_MORE).show()