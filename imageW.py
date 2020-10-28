import PIL
from PIL import Image , ImageFont, ImageDraw,ImageFilter
import os


class MakePhoto:
    GotPhoto = ""
    intCountPhotos = 0



    def __init__(self, img):
        self.GotPhoto = 'static/images/' + img




    def ShowPhoto(self,img):
        imag = Image.open(img)
        imag.show()
        imag.close()

    def FilterPhoto(self):
        imag = Image.open(self.GotPhoto)
        imagF = ImageDraw.Draw(imag)
        font = ImageFont.truetype("Arialn.ttf", size=50)

        imagF.text((20,20), "Hello World", font=font)
        self.intCountPhotos += 1
        ImgName = 'static/images/TC.png'

        imag.save(ImgName)
        imag.close()
        return ImgName

    def BlurImg(self):
        imag = Image.open(self.GotPhoto)
        blurred = imag.filter(ImageFilter.BLUR)
        self.intCountPhotos += 1
        ImgName = 'static/images/bImg.png'

        blurred.save(ImgName)
        blurred.close()
        return  ImgName

    def WitoutColors(self):
        imag = Image.open(self.GotPhoto)
        WitoutColor = imag.filter(ImageFilter.CONTOUR)
        self.intCountPhotos += 1
        ImgName ='static/images/WC.png'

        WitoutColor.save(ImgName)
        WitoutColor.close()
        return  ImgName

    def RotateImg(self):
        imag = Image.open(self.GotPhoto)






