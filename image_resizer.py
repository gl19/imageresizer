from PIL import Image
import os

# change size for (width, height) of image
# for most cases make sure width:height ratio is 16:9
size = (512, 288)
for file in os.listdir():
    if file.endswith('.png') and file != "giesorange.png":
        print(file)
        im = Image.open(file)
        new_image = im.resize(size)
        new_image.save(file)
