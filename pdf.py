from PIL import Image

######----- let the pillow to open the image ----------------######
#######-----from the location and read the image ----------------######

image_1     = Image.open(r'/home/sujan/Documents/NM/1.jpg')
image_2     = Image.open(r'/home/sujan/Documents/NM/2.jpg')
image_3     = Image.open(r'/home/sujan/Documents/NM/3.jpg')
image_4     = Image.open(r'/home/sujan/Documents/NM/4.jpg')
image_5     = Image.open(r'/home/sujan/Documents/NM/5.jpg')
image_6     = Image.open(r'/home/sujan/Documents/NM/6.jpg')
image_7     = Image.open(r'/home/sujan/Documents/NM/7.jpg')
image_8     = Image.open(r'/home/sujan/Documents/NM/8.jpg')
image_9     = Image.open(r'/home/sujan/Documents/NM/9.jpg')
image_10    = Image.open(r'/home/sujan/Documents/NM/10.jpg')

########-------lets conver the image into RGB--------------###### 

im_1      = image_1.convert('RGB')
im_2      = image_2.convert('RGB')
im_3      = image_3.convert('RGB')
im_4      = image_4.convert('RGB')
im_5      = image_5.convert('RGB')
im_6      = image_6.convert('RGB')
im_7      = image_7.convert('RGB')
im_8      = image_8.convert('RGB')
im_9      = image_9.convert('RGB')
im_10     =image_10.convert('RGB')

##### make a list of the images  excluding the first image

image_list = [
    im_2,
    im_3,
    im_4,
    im_5,
    im_6,
    im_7,
    im_8,
    im_9,
    im_10
]

##### save the converted images into pdf 

im_1.save(r'/home/sujan/Documents/NM/nm.pdf', save_all=True, append_images=image_list)
