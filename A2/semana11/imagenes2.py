from PIL import Image

imagenor = Image.open("imagenes/img.png")
imagenor = imagenor.convert("RGB")
imagenor.save("imagenes/imagen2.jpeg","JPEG")