from PIL import Image
import argparse


WIDTH=60
HEIGHT=30
ascii_char=list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
def get_char(r,g,b,alpha=256):
        if alpha==0:
            return ''
        length=len(ascii_char)
        gray=int(0.2126*r +0.7152*g +0.0722*b)
        unit =(256.0+1)/length
        return ascii_char[int(gray/unit)]
if __name__=='__main__':
    im= Image.open("/home/yangchen/pythondemo/sim.jpg")
    im=im.resize((60,30),Image.BILINEAR)

    txt=''
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt+= get_char(*im.getpixel((j,i)))
        txt+='\n'
    print txt
write =open('/home/yangchen/pythondemo/sim.txt','w')
write.write(txt)
write.close()

