from PIL import Image

png_image = Image.open('imageee.png')
jpg_image = png_image.convert('RGB')
jpg_image.save('new.jpg')
