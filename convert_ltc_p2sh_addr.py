#!/usr/bin/python3.6

from hash_util import ripemd160,hash160,hash256,dhash256
from base58 import b58encode,b58encode_check,b58decode,b58decode_check
import binascii

filepath = 'ltc.txt'
def convert(address):
    try:
       decoded = b58decode_check(address);
       version = decoded[:1].hex()
       data    = decoded[1:]
       if   version == '05':     #05:mainet  3xxx
           version = '32'
       elif version == '32':     #50:mainet  Mxxx
           version = '05'
       elif version == 'c4':     #196:testnet 2xxx
           version = '3a'
       elif version == '3a':     #58:testnet Qxxx
           version = 'c4'
       else:
           raise Exception('unknow version {}'.format(version))
       #print (version)

       '''
       05  <-> 50
       196 <-> 58
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

