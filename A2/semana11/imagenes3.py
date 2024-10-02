from PIL import Image

imagen = Image.open("tigre.jpeg")
imagen.resize((300,200)).show()
imagen.rotate(45,expand=True).show()

imagen.transpose(Image.Transpose.FLIP_LEFT_RIGHT).show()
imagen.transpose(Image.Transpose.FLIP_TOP_BOTTOM).show()
imagen.transpose(Image.Transpose.ROTATE_90).show()
imagen.transpose(Image.Transpose.ROTATE_180).show()
imagen.transpose(Image.Transpose.ROTATE_270).show()

#imagen.show()