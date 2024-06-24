from PIL import Image

img = Image.open('./logo_python.png')

# La fonction size renvoie un tuple de deux éléments contenant la largeur et la hauteur de l'image
A COMPLETER = img.size
rgb_im = img.convert('RGB')

for x in range(largeur):
    for y in range(hauteur):
        # La fonction getpixel renvoie un tuple contenant les valeurs RGB du pixel
        A COMPLETER = rgb_im.getpixel((x, y))
        img.putpixel((x, y), (256 - r, 256 - g, 256 - b))
img.show()