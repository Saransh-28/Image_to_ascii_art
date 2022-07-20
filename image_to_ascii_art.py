# import all the required module

from PIL import Image , ImageDraw , ImageFont
import cv2
import numpy as np
import copy

# list of ascii characters according to their densities

ASCII_CHARS = ['$', '@', 'B', '%', '8', '&', 'W', 'M', '#', 'o', 'a', 'h', 'k', 'b', 'd', 'p', 'q', 'w', 'm', 'Z', 'O', '0', 'Q', 'L', 'C', 'J', 'U', 'Y', 'X', 'z', 'c', 'v', 'u', 'n', 'x', 'r', 'j', 'f', 't', '/', '\\', '|', '(', ')', '1', '{', '}', '[', ']', '?', '-', '_','*', '+', '~', '<', '>', 'i', '!', 'l', 'I', ';', ':', ',', '"', '^', '`', "'", '.', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
ASCII_CHARS.reverse()

# define the dimensions of the output image

frame_w = int(input('Enter the width of the output image(NUMBER OF SYMBOLS WORDS)'))
frame_h=int(input('Enter the height of the output image(NUMBER OF SYMBOLS WORDS)'))

# new = Image.new('RGB' , (frame_w*7+50,frame_h*7+50),color=(0,0,0))
new = Image.new('RGB' , (frame_w*7+50,frame_h*7+50),color=(255,255,255))
d = ImageDraw.Draw(new)
font = ImageFont.truetype('The Rift.otf',size=5)

# read the image name and used cv2 to manipulate image

img_name = input('Enter the full name of the image - ')
frame = cv2.imread(img_name)
# convert coloured frame to black and white
black_white = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# resize both the frame , resized coloured frame to get the RGB value
resize = cv2.resize(black_white,(frame_w,frame_h))
frame = cv2.resize(frame,(frame_w,frame_h))

# make an empty array to save the ascii image characters

ascii_image = [['']*resize.shape[1]]*resize.shape[0]
# img_arr = copy.deepcopy(resize)

# take the input 
colour = input('Select the format - \n black/white ( type - "1" ) , colour ( type - "2" ) - ')

#without colour
if colour == '1':
    resize = (85*(resize / 255)).astype(np.int64) 
    for x,row in enumerate(resize):
        for y,element in enumerate(row):
            ascii_image[x][y] = str(ASCII_CHARS[element])
            if ascii_image[x][y] == ' ':
                ascii_image[x][y] += ' '
            # d.text((25+6*y,25+6*x), text='     '+ascii_image[x][y] , fill=(255,255,255),spacing=1,align='center',font=font)
            d.text((25+6*y,25+6*x), text='     '+ascii_image[x][y] , fill=(0,0,0),spacing=1,align='center',font=font)
    new.save(img_name[:-4]+'_bw.jpg')

# RGB
if colour == '2':
    resize = ((resize / 3)).astype(np.int64) 
    for x,row in enumerate(resize):
        for y,element in enumerate(row):
            ascii_image[x][y] = str(ASCII_CHARS[element])
            if ascii_image[x][y] == ' ':
                ascii_image[x][y] == ' '
            color = frame[x][y]
            d.text((25+6*y,25+6*x), text='    '+ascii_image[x][y] , fill=tuple(color),spacing=1,align='center',font=font)
    new.save(img_name[:-4]+'_rgb.jpg')
