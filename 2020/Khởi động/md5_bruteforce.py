from hashlib import md5
import string
from itertools import product
from tqdm import tqdm

for i in tqdm(range(10)):
    for p in product(string.ascii_letters, repeat = i):
        passwd = ''.join(p).encode()
        enc_passwd = md5(passwd).hexdigest()
        if enc_passwd == "c3cef6586e2e5705d9ed18ba8f4346c0":
            print(passwd)
            break
