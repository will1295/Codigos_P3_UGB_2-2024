from PIL import Image

img = Image.open("tigre.jpeg")
img.resize((300,200)).show()
img.rotate(45,expand=True).show()

img.transpose(Image.Transpose.FLIP_LEFT_RIGHT).show()
img.transpose(Image.Transpose.FLIP_TOP_BOTTOM).show()
img.transpose(Image.Transpose.ROTATE_90).show()
img.transpose(Image.Transpose.ROTATE_180).show()
img.transpose(Image.Transpose.ROTATE_270).show()