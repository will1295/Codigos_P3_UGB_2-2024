from PIL import Image

imagen = Image.open("paisaje.jpg")

imagen.convert("L").show()
imagen.convert("P").show()