from PIL import Image

imagen = Image.open("paisaje.jpg")
imgbn = imagen.convert("L").show()
imgp = imagen.convert("P").show()