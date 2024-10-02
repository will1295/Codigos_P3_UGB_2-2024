from PIL import Image

img = Image.open("logo2.png")

traspo1 = img.transpose(Image.FLIP_LEFT_RIGHT)
traspo2 = img.transpose(Image.FLIP_TOP_BOTTOM)
traspo3 = img.transpose(Image.ROTATE_90)
traspo4 = img.transpose(Image.ROTATE_180)
traspo5 = img.transpose(Image.ROTATE_270)
traspo1.show()
traspo2.show()
traspo3.show()
traspo4.show()
traspo5.show()