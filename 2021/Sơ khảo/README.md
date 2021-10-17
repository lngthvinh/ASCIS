# ASEAN STUDENT CONTEST ON INFORMATION SECURITY 2021

### Overview
 | Title | Category | Points | Flag
 | ------ | ------ | ------ | ------ |
 | [Hello world](#Hello-world) | MISC | 100 | `ASCIS{th1$_1$_4_fl4g}` |
 | [PNG](#PNG) | MISC | 100 | `ASCIS{png_h1dd3n_d4t4}` |
 | [travel paper](#travel-paper) | MISC | 100 | `ASCIS{c0r0n4_v1rus_1s_g0n3}` |
 | Sherlock Homes | MISC | 451 |  |
 | echo server | Pwnable | 100 |  |
 | Guessme | Pwnable | 200 |  |
 | Keygen me | Reverse | 100 |  |
 | [Decrypt me](#Decrypt-me) | Reverse | 200 | `ASCIS{x0r_me_t0_get_the_flag}` |
 | [Simple For](#Simple-For) | Misc | 100 | `ASCIS{n3tw0rk_f0r3ns1c_1s_n0t_h4rd}` |
 | [Calculate me](#Calculate-me) | Misc | 100 | `ASCIS{3v3ry0n3_sh0uld_kn0w_pr0gramm1ng}` |
 
# Hello world
 
### Challenge
 
<img src=files/1.png>
 
### Solution

* Tìm trong source của trang web.

<img src=files/2.png>

# PNG
 
### Challenge
 
<img src=files/3.png>

[vcs.png](files/vcs.png)

### Solution

* Ta nhận được file png.

<img src=files/4.png>

* Vậy cờ nằm ở phần còn lại của bức hình. Sử dụng công cụ [TweakPNG](http://entropymine.com/jason/tweakpng/) để thay đổi size hình.

<img src=files/5.png>

* Sau khi thay đổi, ta có phần còn lại của hình có chứa cờ.

<img src=files/6.png>

# travel paper
 
### Challenge
 
<img src=files/7.png>
 
### Solution

* Truy cập netcat ta được QR Code.

<img src=files/8.png>

* Viết chương trình tự động submit qr code.

*(Code này của anh Hiếu team mình, anh Hiếu code python để đọc QR Code xịn lắm nghen 😆)*

* Code bạn đọc tham khảo có thể lấy ở đây:
* [qrcode_solve.py](file/qrcode_solve.py)
* [clacon.ttf](file/clacon.ttf)

```python
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


```

* Kết quả chạy đến qr code thứ 100 là có cờ.

<img src=files/9.png>

# Sherlock Homes
 
### Challenge
 
<img src=>
 
### Solution

* Tìm trong source của trang web.

<img src=>






















