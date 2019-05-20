from PIL import Image

##### used to compress an image to be transferred to marketing clients for dispaly
basewidth = 300
img = Image.open("/Users/ankitkumar/Downloads/desktop-background.jpg")

wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
img.save('/Users/ankitkumar/Downloads/resized_image.jpg')
