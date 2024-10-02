from PIL import Image

imagen_or = Image.open("tigre.png")
imagen_du = imagen_or.save("tigre2.jpg")
imagen2 = Image.open("tigre2.jpg")
imagen2.show()