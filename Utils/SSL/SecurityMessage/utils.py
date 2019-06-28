from OpenSSL import crypto
from OpenSSL.crypto import load_certificate,load_pkcs12,FILETYPE_PEM,dump_publickey,dump_privatekey
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

class tool(object):
    @classmethod
    def RSA_encrypt(cls,data,public_key):
        key= load_certificate(FILETYPE_PEM, open(public_key, 'rb').read())
        key_buffer = dump_publickey(FILETYPE_PEM, key.get_pubkey())

        # 从公钥数据中加载公钥
        public_key = serialization.load_pem_public_key(
            key_buffer,
            backend=default_backend()
            )

        # 使用公钥对原始数据进行加密，使用PKCS#1 v1.5的填充方式
        out_data = public_key.encrypt(
            data,
            padding.PKCS1v15()
        )

        return out_data

    @classmethod
    def RSA_decrypt(cls,cipher_text,private_key,password='123456'):

        key = load_pkcs12(open(private_key, 'rb').read(), password)
        key_buffer= dump_privatekey(FILETYPE_PEM, key.get_privatekey())


        # 从私钥数据中加载私钥
        private_key = serialization.load_pem_private_key(
            key_buffer,
            password=None,
            backend=default_backend()
        )

        # 使用私钥对数据进行解密，使用PKCS#1 v1.5的填充方式
        out_data = private_key.decrypt(
            cipher_text,
            padding.PKCS1v15()
        )

        return out_data


    @classmethod
    def sign(cls,data,private_key,password='123456'):
        key = load_pkcs12(open(private_key, 'rb').read(), password).get_privatekey()
        signatrue=crypto.sign(key, data, digest='sha1')
        return signatrue

    @classmethod
    def verify(cls,data,signatrue,public_key):
        key = load_certificate(FILETYPE_PEM, open(public_key, 'rb').read())
        try:
           crypto.verify(key,signatrue,data,digest='sha1')
           return True
        except Exception as e:
            print(e)
            return False







