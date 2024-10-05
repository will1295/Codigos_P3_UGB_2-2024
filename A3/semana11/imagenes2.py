from PIL import Image

img = Image.open("tigre.jpeg")
img.save("imagenes/tigre.png")
img.show()

img2 = Image.open("img.png")
ima = img2.convert("RGB")
ima.save("imagenes/img.jpeg")
ima.show()