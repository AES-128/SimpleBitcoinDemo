from hashlib import sha256
import struct
import requests
import sys

MAX_NONCE = 0xFFFFFFFF
zeroes = 4 # difficulty

if len(sys.argv) < 2:
    print("Usage: python bitcoin.py <block_height>")
    print("A simple script that demonstrates how the mining process in Bitcoin works.")
    print("Generates a random nonce and repeatedly hashes until the required number of zeroes (difficulty) is found.\n")
    exit(1)

# Retrieve the data for a block

block_height = int(sys.argv[1])
r = requests.get(f"https://blockchain.info/block-height/{block_height}?format=json").json()
data = r["blocks"][0]

little_endian = lambda x: struct.pack("<L", x)

# Create block header

block_header = bytearray()
block_header += little_endian(data["ver"])
block_header += bytearray.fromhex(data["prev_block"])[::-1]
block_header += bytearray.fromhex(data["mrkl_root"])[::-1]
block_header += little_endian(data["time"])
block_header += little_endian(data["bits"])

# Brute force through nonce values

for nonce in range(MAX_NONCE):
    new_header = block_header + struct.pack("<L", nonce)
    hash_ = sha256(sha256(new_header).digest()).digest()

	# If we have the correct number of leading zeroes, the block is valid

    if hash_[-zeroes:] == b"\x00" * zeroes:
        print("[+] Block mined!")
        print(f"\tHash: 0x{hash_[::-1].hex()}")
        print(f"\tNonce: {nonce}")
        break
