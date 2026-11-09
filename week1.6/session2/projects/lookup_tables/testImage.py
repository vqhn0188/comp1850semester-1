from image import Image
list = list(range(256))
for i in list:
    list[i] = 255 - i
image = Image.read("coins.pgm")
size = image.width * image.height
for i in range(size):
    image[i] = list[image[i]]

image.write_pgm("flipped_coin.pgm")