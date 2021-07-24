#download the pillow module
#pip install pillow

from PIL import Image, ImageDraw, ImageFont,ImageEnhance, ImageFilter,ImageOps
import PIL

#keep this sample photo in the same folder as same as the python file
img = PIL.Image.open('image.jpg')

print("Enter which operation would you like to perform?\n")
ch = int(input("Enter any of these char for specific operation:\n\n 1: For Black and White Effect \n 2: For Brightness Enhancement \n 3: For Color Enchancement \n 4: for Blurry Effect \n 5: For Contrast \n 6: For Posterizing \n 7: For Inverting \n 8: For Cropping \n 9: For Rotation \n 10: For Mirroring \n 11: For thumbnail \n 12: To add text \n 13: To add logo \n 14: To Compress: \n"))

print(ch)
if ch ==1:
    #changes the image to black and white
    image_file = img.convert('1') 
    image_file.save('blacknWhite.png')


elif ch==2:
    #increases the brightness
    n2=int(input("Enter the value for brightness enhancement: "))
    converter = PIL.ImageEnhance.Brightness(img).enhance(n2)
    converter.save('brightness.png')


elif ch==3:
    #increases color of the image
    print("enter the value for color enhancement")
    n3=int(input())
    converter = PIL.ImageEnhance.Color(img).enhance(n3)
    converter.save('color.png')


elif ch == 4:
    #for bluring an image
    print("enter the value of bluriness")
    n4=int(input())
    blur = img.filter(ImageFilter.GaussianBlur(radius = n4)) 
    blur.save('blur.png') 


elif ch == 5:
    #for contrasting image
    print("enter the value of contrasting")
    n5=int(input())
    converter = PIL.ImageEnhance.Contrast(img).enhance(n5)
    converter.save('Contrast.png')


elif ch ==6:
    #for posterizing the image
  
    im = ImageOps.posterize(img, 20)  
    im.save('posterize.png')


elif ch ==7:
    #for inverting the image
    inverted_image = PIL.ImageOps.invert(img)
    inverted_image.save('invert.png')


elif ch == 8:
    #for cropping the image
    #coordinates for cropping size is fixed but can be changed in this code
    crop = img.crop((0, 0, 2500, 2500))
    crop.save('crop.png')


elif ch== 9:
    #for rotating the image
    print("enter the angle for rotation")
    n7=int(input())
    rotate = img.rotate(n7)
    rotate.save('rotate.png')


elif ch== 10:
    #mirror effect of the image
    im_mirror = ImageOps.mirror(img)
    im_mirror.save('mirror.png')


elif ch==11:
    #to make a thumbnail
    th = Image.open("image.jpg")  
    #In-place modification 
    th.thumbnail((200, 200))  
    th.save("thumb.png") 

elif ch==12:
    #for adding text
    n8=input("enter your text: ")
    n9=input("enter color code: ")
    n10=int(input("enter font size: "))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('arial.ttf', size=n10)
    #coordinates of text
    draw.text((50, 50),n8,fill = n9, font=font)
    img.save('draw.png')


elif ch == 13:
    #adding logo or watermark
    til = Image.open('pin.png')
    #coordinates for new photo
    img.paste(til,(100,50))
    img.save('paste.png')



elif ch == 14:
    #for compressing the image
    #lower the quality higher the compression
    n10=int(input("enter the quality: "))
    img.save("compress.png",optimize=True,quality= n10)

else:
    print("wrong input!!")
