#!/usr/bin/python3.6

from hash_util import ripemd160,hash160,hash256,dhash256
from base58 import b58encode,b58encode_check,b58decode,b58decode_check
import binascii

filepath = 'btc.txt'
def convert(address):
    try:
       decoded = b58decode_check(address);
       version = decoded[:1].hex()
       data    = decoded[1:]
       if version == '26':       #p2pkh Gxx
           version = '00'
       elif version == '00':     #p2sh 1xx
           version = '26'
       elif version == '17':     #p2sh Axx
           version = '05'
       elif version == '05':     #p2sh 3xx
           version = '17'
       else:
           raise Exception('unknow version {}'.format(version))
       #print (version)

       '''
       05  <-> 23
       00  <-> 26
       '''
       #print (version+data.hex())
       newAddress = b58encode_check( bytes.fromhex(version+data.hex()) )
       #print (newAddress)
    except:
        return address
    return str(newAddress, 'utf-8')

with open(filepath) as fp:
    line = fp.readline()
    while line:
        address = line.strip()
        if address == '':
            line = fp.readline()
            continue
        address = convert(address)
        print(line.strip() +'\t'+ address)
        line = fp.readline()

