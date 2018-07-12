import sys
from PIL import Image, ImageDraw, ImageOps

def open_image(image_path):
    return Image.open(image_path)


def create_thumbnail(image, thumbnail_size=None):
    size = ()
    if thumbnail_size != None:
        size = (thumbnail_size, thumbnail_size)
    
    else:
        image_width = image.width
        image_height = image.height
        if image_width > image_height:
            size = (image_height, image_height)
        else:
            size = (image_width, image_width)
    
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
    try:
        assert(len(sys.argv) > 1)

    except AssertionError:
        print("Error. Did not supply image path")
        return(-1)
    print(str(sys.argv))
    thumbnail_size = 256
    if '--size' in sys.argv:
        size_flag_index = sys.argv.index('--size')
        thumbnail_size = int(sys.argv[size_flag_index+1])
    source_image = open_image(sys.argv[-1])
    create_thumbnail(source_image, thumbnail_size).show()
main()
#im = open_image("test.jpg")
#im.show()
#create_thumbnail(im,256).show()
#create_thumbnail(im).show()
