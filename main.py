from PIL import Image, ImageDraw, ImageFont,ImageColor    
from inputdata import *
def findfont(text_bbox,box_width,box_height,font,fontsize,text,draw):
    while text_bbox[2] > box_width-10 or text_bbox[3] > box_height:
        fontsize -= 1
        font = ImageFont.truetype(font_used, fontsize)
        text_bbox = draw.textbbox((0, 0), text, font=font)
    return font

def imagetranform(text1,text2,path):
    # Image Open
    image = Image.open(path)
    print(image.size)
    right = 0
    left = 100
    top = 50
    bottom = 300
    width, height = image.size
    # Adding the Padding for the text
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(image.mode, (new_width, new_height), (255, 255, 255))
    draw = ImageDraw.Draw(result)
    # Adding the grey box behind
    draw.rectangle((0, 0, new_width, height/2+50), fill=ImageColor.getrgb("#f4f4f6"))
    # Adding the Image
    result.paste(image, (left, top))
    # First font calculation
    font = ImageFont.truetype(font_used, 45)
    draw = ImageDraw.Draw(result)
    draw.rectangle((0, height+50, new_width/2, height+100), fill=ImageColor.getrgb("#dfcad1"))
    draw.rectangle((new_width/2, height+50, new_width, height+100), fill=ImageColor.getrgb("#2b1e16"))
    text_bbox = draw.textbbox((10, 0), text1, font=font)
    font=findfont(text_bbox,width-500,45,font,45,text1,draw)
    # Adding Text1
    draw.text((new_width/4,new_height-270), text1, font=font, fill= ImageColor.getrgb("#fffbfe"),anchor='mm') 
    box_width,box_height=new_width,250
    # Second font calculation
    font = ImageFont.truetype(font_used, 150)
    text_bbox = draw.textbbox((0, 0), text2, font=font)
    font = findfont(text_bbox,box_width,box_height,font,150,text2,draw)
    # Adding Text2
    draw.text((new_width/2,height+250), text2, font=font, fill= ImageColor.getrgb("#48433f"),anchor='mm') 
    result.save('output.png')


imagetranform(text1,text2,path)