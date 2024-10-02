from PIL import Image

imagen_or = Image.open("tigre.jpeg")
imagen_du = imagen_or.save("tigre.png")
imagen2 = Image.open("tigre.png")
imagen2.show()
