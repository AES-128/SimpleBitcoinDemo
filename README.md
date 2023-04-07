# SimpleBitcoinDemo

A simple script that demonstrates how the mining process in Bitcoin works.

Generates a random nonce and repeatedly hashes until the required number of zeroes (difficulty) is found.

# Usage

```python
$ python bitcoin.py <block_height>
```

For example, to mine the Genesis Block ...

```python
$ python3 main.py 0

... couple hours later ...

[+] Block mined!
    Hash: 0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
    Nonce: 2083236893
```

<sub>Please note that it is not optimised for speed (so don't try mining with this), this is purely for demonstrative purposes.</sub>
