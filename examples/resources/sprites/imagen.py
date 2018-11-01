from PIL import Image

basewidth = 300
img = Image.open('circle.png')
#box = (10, 100, 500, 900)
#1920 / 96 = 20
#Escala a 20
#800 x 400

width, height = img.size
width  = int(width / 10)
height = int(height / 10)

img = img.resize((150, 150), Image.ANTIALIAS)
img.save('medium_circle.png')
