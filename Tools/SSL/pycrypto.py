# -*- coding: utf-8 -*-
#author:'lijunbo'
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
from OpenSSL.crypto import load_certificate,load_pkcs12,FILETYPE_PEM,dump_publickey,dump_privatekey
path1='mer-public-rsa.cer'
path2='mer-private-rsa.pfx'

# str1=load_pkcs12(open(path2,'rb').read(),'123456')
# str2=load_certificate(FILETYPE_PEM,open(path1,'rb').read())
# key1=dump_privatekey(FILETYPE_PEM,str1.get_privatekey()) .decode()
# key2=dump_publickey(FILETYPE_PEM,str2.get_pubkey()).decode()

# 伪随机数生成器
random_generator = Random.new().read
# rsa算法生成实例
rsa = RSA.generate(1024, random_generator)

# master的秘钥对的生成
# private_pem = rsa.exportKey()

# with open('ghost-private.pem', 'wb') as f:
#     f.write(private_pem)
#
# public_pem = rsa.publickey().exportKey()
# with open('ghost-public.pem', 'wb') as f:
#     f.write(public_pem)
#公钥加密，私钥解密
class tool(object):
    @classmethod
    def  RSA_encrypt(cls,message,pem_path):
        str2 = load_certificate(FILETYPE_PEM, open(path1, 'rb').read())
        key2 = dump_publickey(FILETYPE_PEM, str2.get_pubkey()).decode()
        rsakey = RSA.importKey(key2)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        cipher_text = cipher.encrypt(message)
        return cipher_text
    
    @classmethod
    def RSA_decrypt(cls,cipher_text,pem_path):


        str1 = load_pkcs12(open(path2, 'rb').read(), '123456')
        key1 = dump_privatekey(FILETYPE_PEM, str1.get_privatekey()).decode()

        print(key1)
        rsakey = RSA.importKey(key1)
        cipher = Cipher_pkcs1_v1_5.new(rsakey)
        text = cipher.decrypt(cipher_text, random_generator)
        return text
        # assert text == message, 'decrypt falied'

    
    #签名
    @classmethod
    def signatrue(cls,message,pem_path):
        with open(pem_path,'rb') as f:
            key = f.read()
            rsakey = RSA.importKey(key)
            signer = Signature_pkcs1_v1_5.new(rsakey)
            digest = SHA.new()
            digest.update(message)
            sign = signer.sign(digest)
            return sign
    
    
    #验签
    @classmethod
    def verify(cls,message,sign,pem_path):
        with open(pem_path,'rb') as f:
            key = f.read()
            rsakey = RSA.importKey(key)
            verifier = Signature_pkcs1_v1_5.new(rsakey)
            digest = SHA.new()
            digest.update(message)
            is_verify = verifier.verify(digest, sign)
            return is_verify

if __name__=="__main__":
    str=tool.RSA_encrypt(b'junbo',path2)
    print(str)
    str2=tool.RSA_decrypt(str,path1)
    print(str2)