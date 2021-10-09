# ASEAN STUDENT CONTEST ON INFORMATION SECURITY 2021

### Overview
 | Title | Category | Points | Flag
 | ------ | ------ | ------ | ------ |
 | [Simple For](#Simple-For) | Misc | 100 | `ASCIS{n3tw0rk_f0r3ns1c_1s_n0t_h4rd}` |
 | [Calculate me](#Calculate-me) | Misc | 100 | `ASCIS{n3tw0rk_f0r3ns1c_1s_n0t_h4rd}` |
 
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

<img src=files/193213.png>
