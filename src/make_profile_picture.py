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

    resized_image = ImageOps.fit(image, circle_overlay.size, centering=(0.5, 0.5))
    resized_image.putalpha(circle_overlay)
    return resized_image
    

# im = open_image("test.jpg")
# create_thumbnail(im,256).show()
# create_thumbnail(im).show()