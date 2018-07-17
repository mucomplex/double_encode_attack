#!/usr/bin/python3
import os
import sys
import urllib.parse as encode

def help():
    usage = '''[*] double_encode_attack.py http://url/'''
    print(usage)

class encoder():
    def __init__(self,value):
        self.value = value
    def single_encode(self):
        init = str(self.value).replace(' ','my_space')
        return encode.quote_plus(init).replace('my_space','%20')
    
    def double_encode(self):
        return encode.quote_plus(self.single_encode())

if(len(sys.argv) != 2):
    help()
else:
    my_value = sys.argv[1]
    my_encoder = encoder(my_value)
    print(my_encoder.single_encode())
    print(my_encoder.double_encode())
