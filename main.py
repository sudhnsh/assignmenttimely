from PIL import Image, ImageDraw, ImageFont,ImageColor    
from inputdata import *
def findfont(text_bbox,box_width,box_height,font,fontsize,text,draw):
    while text_bbox[2] > box_width-10 or text_bbox[3] > box_height:
        fontsize -= 1
        font = ImageFont.truetype(font_used, fontsize)
        text_bbox = draw.textbbox((0, 0), text, font=font)
    return font

def ratio_cal(width,height):
    ratio= height/width
    if height>width:
        new_height=730
        new_width=round(730/ratio)
    else :
        new_width=980
        new_height=round(980*ratio)
    return (new_width,new_height)

def imagetranform(text1,text2,path):
    # Image Open
    image = Image.open(path)
    print(image.size)
    new_width,new_height=ratio_cal(image.size[0],image.size[1])
    image = image.resize((new_width,new_height))
    print(image.size)
    width, height = image.size
    # Adding the Padding for the text
    result = Image.new(image.mode, (1080,1080), (255, 255, 255))
    draw = ImageDraw.Draw(result)
    # Adding the grey box behind
    draw.rectangle((0, 0, 1080, height/2+50), fill=ImageColor.getrgb("#f4f4f6"))
    # Adding the Image
    result.paste(image, (1080-width, 50))
    # First font calculation
    font = ImageFont.truetype(font_used, 45)
    draw = ImageDraw.Draw(result)
    draw.rectangle((0, height+50, 540, height+100), fill=ImageColor.getrgb("#dfcad1"))
    draw.rectangle((540, height+50, 1080, height+100), fill=ImageColor.getrgb("#2b1e16"))
    text_bbox = draw.textbbox((10, 0), text1, font=font)
    font=findfont(text_bbox,580,45,font,45,text1,draw)
    # Adding Text1
    draw.text((270,height+72.5), text1, font=font, fill= ImageColor.getrgb("#fffbfe"),anchor='mm') 
    box_width,box_height=1080,250
    # Second font calculation
    font = ImageFont.truetype(font_used, 150)
    text_bbox = draw.textbbox((0, 0), text2, font=font)
    font = findfont(text_bbox,box_width,box_height,font,150,text2,draw)
    # Adding Text2
    draw.text((540,height+250), text2, font=font, fill= ImageColor.getrgb("#48433f"),anchor='mm') 
    result.save('output.png')


imagetranform(text1,text2,path)