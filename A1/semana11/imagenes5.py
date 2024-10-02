from PIL import Image

imagent = Image.open("tigre.png")

transpo1 = imagent.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
transpo1.show()

transpo2 = imagent.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
transpo2.show()

transpo3 = imagent.transpose(Image.Transpose.ROTATE_90)
transpo3.show()

transpo4 = imagent.transpose(Image.Transpose.ROTATE_180)
transpo4.show()

transpo5 = imagent.transpose(Image.Transpose.ROTATE_270)
transpo5.show()