import binascii
import hashlib

def hash256(input):
    result=hashlib.new('sha256', input).digest()
    return result

def ripemd160(input):
    result=hashlib.new('ripemd160', input).digest()
    return result

def hash160(input):
    data = hash256(input)
    return ripemd160(data)

def dhash256(input):
    data = hash256(input)
    return hash256(data)

def formatamount(amount):
    hex_bits=hex(amount).lstrip('0x').rstrip('L')
    if (len(hex_bits) % 2 == 1):
        hex_bits = "0"+hex_bits

    data=reverse_byte_order(hex_bits)
    return data.ljust(16, '0')

def reverse_byte_order(input):
     data = binascii.unhexlify(input)[::-1].encode('hex')
     return data

def get_len_hex(input):
    length=(len(input))/2
    return length

