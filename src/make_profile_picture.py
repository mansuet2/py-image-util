#!/usr/bin/env python
import sys
from PIL import Image, ImageDraw, ImageOps

class ThumbnailMaker:
    def __init__(self, filepath=None, size=None):
        self.default_size=256

        if filepath is not None:
            self.filepath = filepath
        if size is not None:
            self.default_size = size 

    def create(self, input_fp, output_fp, size=None):
        if size is None:
            size = self.default_size 

        image = self.open(input_fp)
        new_image = self.create_thumbnail(image, size)
        self.save(new_image,output_fp)
        image.close()

    def open(self, image_path):
        return Image.open(image_path)

    def save(self, image, filepath):
        image.save(filepath + ".png")
    
    def create_thumbnail(self, image, thumbnail_size=None):
        if thumbnail_size is None:
            thumbnail_size = self.default_size

        size = (int(thumbnail_size), int(thumbnail_size))
        
        circle_overlay = Image.new('L', size, 0)
    
        circle_draw = ImageDraw.Draw(circle_overlay)
    
        circle_draw.ellipse(
            [(0,0), size],
            fill=255,
        )
    
        resized_image = ImageOps.fit(image, circle_overlay.size, Image.ANTIALIAS, centering=(0.5, 0.5))
        resized_image.putalpha(circle_overlay)
        return resized_image

def main():
    my_maker = ThumbnailMaker()
    try:
        assert(len(sys.argv) > 1)
    except AssertionError:
        print("Error. Did not supply image path")
        return(-1)
    if '--help' in sys.argv:
        print("Usage: ./make_profile [--size] in.jpg out.jpg")
    elif '--size' in sys.argv:
        try:
            assert sys.argv[1] == '--size'
        except AssertionError:
            print("Error: --flag must come after command.\nUsage: ./make_profile_picture.py --size 512 in.jpg out.jpg")
            return -1

        thumbnail_size = sys.argv[2]
        my_maker.create(sys.argv[3], sys.argv[4], thumbnail_size)   
    else:
        my_maker.create(sys.argv[1], sys.argv[2])
main()
