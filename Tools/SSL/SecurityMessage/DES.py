from pyDes import *
class C(object):

    @classmethod
    def des_encrypt(cls,paramString1,paramString2):

        Des_Key=Des_IV=paramString2
        k = des(Des_Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)
        # Key must be exactly 8 bytes long
        EncryptStr = k.encrypt(paramString1)
        return EncryptStr

    @classmethod
    def des_decrypt(cls,paramString1,paramString2):
        Des_Key = Des_IV = paramString2
        k = des(Des_Key, CBC, Des_IV, pad=None, padmode=PAD_PKCS5)
        DecryptStr=k.decrypt(paramString1)
        return DecryptStr

