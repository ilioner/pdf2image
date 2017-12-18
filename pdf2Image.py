# !/usr/bin/python
# -*- coding: utf-8 -*-

from wand.image import Image
from wand.api import library
from wand.compat import binary

class wimage(Image):
    def myDefine(self, key, value):
        """ Skip over wand.image.Image.option """
        return library.MagickSetOption(self.wand, binary(key), binary(value))


def pdf2image(filename="",format="jpeg",width=100,height=100,quality=100,outdir="",filename_format=""):
    with wimage(filename=filename, resolution=300) as img:
        for i in range(len(img.sequence)):
            ftemp='%s/%s%i.jpg'%(outdir,filename_format,i)
            with wimage(img.sequence[i]) as img_to_save:
                img_to_save.myDefine('jpeg:extent', '2000kb')
                img_to_save.compression_quality = quality
                img_to_save.resize(width, height)
                img_to_save.format= format
                img_to_save.save(filename= ftemp)


pdf2image(filename="image.pdf",format="jpeg",width=2400,height=3324,quality=300,outdir="image",filename_format="img_")


