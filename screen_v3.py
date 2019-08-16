from PIL import Image, ImageDraw
import pytesseract
import os
import PIL.ImageOps 
from time import sleep

def fuction_time(func):
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper

def get_text_eng(image):
    return pytesseract.image_to_string(image, lang = 'eng')

def get_text_rus(image):
    return pytesseract.image_to_string(image, lang = 'rus')

def get_balck_white(image):

    draw = ImageDraw.Draw(image) 

    width = image.size[0]  

    height = image.size[1] 	

    pix = image.load() 

    factor = 85
    for i in range(width):
        for j in range(height):
            a = pix[i, j][0]
            b = pix[i, j][1]
            c = pix[i, j][2]
            S = a + b + c
            if (S > (((255 + factor) // 2) * 3)):
                    a, b, c = 255, 255, 255
            else:
                    a, b, c = 0, 0, 0
            draw.point((i, j), (a, b, c))

    return image


@fuction_time
def main(screen):
    image = screen.crop( (265,314,402,727) )
    image = get_balck_white(image)
    a = []
    for i in pytesseract.image_to_string(image, lang = 'rus').split('\n'):
        a.append(i)
    names = [x for x in a if x]

    image = screen.crop( (728,314,860,727) )
    image = get_balck_white(image)
    a = []
    for i in pytesseract.image_to_string(image, lang = 'rus').split('\n'):
        a.append(i)
    nicks = [x for x in a if x]
    y = 0
    for i in range(len(names)):
        money = screen.crop( (454, 313 + y, 724, 358 + y) )
        qqq = pytesseract.image_to_string(money, lang = 'eng')
        price = qqq.split('@')[0].replace(' ','')
        one_price = qqq.split('@')[1].replace("@","").replace(" ", "")

        
        img = screen.crop( (400, 313 + y, 862, 358 + y) )
        img = get_balck_white(img)
        al = get_text_eng(img).replace("\n", ' ')
        al = al.split('@')
        nick = al[len(al)-1]
        qq = al[0].split(' ')
        lvl = qq[0]
        print(str(int(price)//int(one_price)),names[i], lvl, price, one_price, nick + " | " + nicks[i].replace(",",''))
        y += 47.5
        
im = PIL.ImageOps.invert(Image.open("main.png", mode = 'r'))
main(im)
