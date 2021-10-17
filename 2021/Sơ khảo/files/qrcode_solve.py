#!/usr/bin/python3
from PIL import Image, ImageFont, ImageDraw
from pyzbar.pyzbar import decode


def qrimg(lines, filename, sub=1):
    size_ = 500
    font = ImageFont.truetype('clacon.ttf', size=20)  
    img=Image.new("RGBA", (size_, size_),(255,255,255))
    draw = ImageDraw.Draw(img)  
    y_text = 8
    for line in lines:  
        # line = unicode(line, "utf-8")
        width, height = font.getsize(line)
        draw.text((0,y_text),line,(0,0,0), font=font)  
        y_text += height - sub
        draw = ImageDraw.Draw(img)  
    img.save(filename)

# Hàm này nhận một dòng (line) từ socket
def receive_one_line(s):
    r = b''

    # Lần lượt nhận từng ký tự, nếu là ký tự xuống dòng thì ngưng
    while (True):
        t = s.recv(1)
        if t == b'\n': break
        r = r + t

    # Trả về kết quả dạng string
    return r.decode()

# Hàm này gửi một dòng (line) đến socket
def send_one_line(s, data):
    # Bỏ hết ký tự xuống dòng trong data (nếu có) và gửi đến server
    data = data.strip()
    s.send((data + '\n').encode())

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('125.235.240.166',20123))

banner = receive_one_line(s)
print(banner)

while('ASCIS{' not in banner):
    banner = receive_one_line(s)
    print(banner)
    save = []
    if 'Person' in banner:
        banner = receive_one_line(s)
        banner = receive_one_line(s)
        banner = receive_one_line(s)
        while(banner.strip() != ''):
            print(banner)
            save.append(banner)
            banner = receive_one_line(s)

        data = ''
        flag = False
        sub = 0.8
        while(flag == False and sub < 1.1):
            print(f"Sub: {sub}")
            qrimg(save, 'sub.png', sub)
            data = decode(Image.open('sub.png'))[0].data.decode()
            # if there is a QR code
            # print the data
            if data != '':
                print(f"QRCode data: {data}")
                flag = True
            else:
                sub += 0.1
        
        data = data.split('|')
        send_one_line(s, data[0])
        send_one_line(s, data[1])
        send_one_line(s, data[2])

