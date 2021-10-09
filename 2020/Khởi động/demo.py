from hashlib import sha256
from base64 import b64encode, b64decode

from typing import Tuple
ByteStrings = Tuple[bytes, ...]


def h(s: bytes) -> bytes:
    """Short notation for sha256. The digest is truncated to 6 bytes to save
    bandwidth."""
    return sha256(s).digest()[:6]


def merkle_hash(byte_strings: ByteStrings) -> bytes:
    """Get the root hash of a Merkle tree built from given byte strings. For
    more information, please visit https://en.wikipedia.org/wiki/Merkle_tree.
    """
    hashes = [h(s) for s in byte_strings]
    while len(hashes) > 1:
        if len(hashes) % 2 == 1:
            hashes.append(hashes[-1])
        hashes = [h(hashes[i] + hashes[i+1]) for i in range(0, len(hashes), 2)]
    return hashes[0]

from string import ascii_letters
from itertools import combinations
from tqdm import tqdm

if __name__ == "__main__":
    # n = 1
    # a = set()
    # for n in tqdm(range(1, 2021)):
    #     for i in combinations(ascii_letters, n):
    #         p = set()
    #         for c in i:
    #             p.add(c.encode())
    #         t = merkle_hash(p)
    #         if t not in a:
    #             a.add(t)
    #         else: 
    #             print('Warning!')
    #             print(i)
    transaction1 = [b'a',b'b',b'c',b'd']
    transaction2 = [b'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d',b'2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc618ac3e7343f016890c510e93f935261169d9e3f565436429830faf0934f4f8e4']
    transaction3 = [b'62af5c3cb8da3e4f25061e829ebeea5c7513c54949115b1acc225930a90154dad3a0f1c792ccf7f1708d5422696263e35755a86917ea76ef9242bd4a8cf4891a']
    
    print(merkle_hash(transaction1))
    print(merkle_hash(transaction2))
    print(merkle_hash(transaction3))

    a = [b'a',b'b',b'c']
    print(merkle_hash(a))
