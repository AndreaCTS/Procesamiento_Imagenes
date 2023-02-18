from PIL import Image,ImageFilter,ImageEnhance
im = Image.open("Photos/mdb001.pgm")

print(im.format, im.size, im.mode)


im = im.convert("L")

#r, g, b = im.split()
#im = Image.merge("RGB", (b, g, r))

# multiply each pixel by 1.2
out = im.point(lambda i: i * 1.2)
#out = im.filter(ImageFilter.DETAIL)

enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show("30% more contrast")

#im = Image.NEAREST(im)

im.show()
