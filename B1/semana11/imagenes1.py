from PIL import Image

img = Image.open("imagen.png")
#img.show()
#img.save("logo.png")
imgc=img.convert("RGB")
imgc.save("logo.jpeg")