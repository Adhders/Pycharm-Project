import base64
import random
import string
from SecurityMessage.utils import tool
from SecurityMessage.DES import C

def encrypt(data,public_key,private_key,password):
    str = ''.join(random.sample(string.ascii_letters + string.digits, 8)).encode()
    if not isinstance(data,bytes):
        data=data.encode()
    byte1=tool.RSA_encrypt(str,public_key)
    byte2=C.des_encrypt(data,str)
    byte3=byte1[:]+byte2[:]
    byte4=tool.sign(byte3,private_key,password)
    byte5=byte4[:]+byte3[:]
    return base64.b64encode(byte5).decode('utf-8')

def decrypt(data,pubkeypath,prikeypath,password):
     data=base64.b64decode(data)
     byte1=data[:128]
     i=len(data)
     j=i-128
     byte2=data[128:i]
     bool=tool.verify(byte2,byte1,pubkeypath)
     if bool:
         byte3=byte2[:128]
         str3=tool.RSA_decrypt(byte3,prikeypath,password)
         byte4=byte2[128:j]
         str=C.des_decrypt(byte4,str3).decode('utf-8')
     return str


