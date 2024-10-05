from PIL import Image

img = Image.open("paisaje.jpg")

img.convert("L").show()
img.convert("P").show()