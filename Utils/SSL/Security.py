from SSL import A

import os
class SecurityMessageCrypto(object):

    @classmethod
    def shop(cls,paramString):
        i=0
        if paramString:
            i=len(paramString)
        if i>20:
            raise ValueError('商户编号超过20位')

        arrayOfChar=['#']*(20-i)
        str=''.join(arrayOfChar)
        if i>0:
            paramString=paramString+str
        else:
            paramString=str
        return paramString

    @classmethod
    def OpenSecurityMessage(cls,cipher,pubkeypath,prikeypath,pwd):
        cipher=cipher[20:]
        return A.decrypt(cipher, pubkeypath, prikeypath, pwd)

    @classmethod
    def MakeSecurityMessage(cls,message,pubkeypath,prikeypath,pwd,shopId):
        paramString=cls.shop(shopId)
        return paramString + A.encrypt(message, pubkeypath, prikeypath, pwd)


if __name__=="__main__":

    pubkeypathA='mer-public-rsa.cer'
    prikeypathA='mer-private-rsa.pfx'
    pubkeypathB='pccc-public-rsa.cer'
    prikeypathB='pccc-private-rsa.pfx'
    cipher="'123456789012345#####gvUxsBHu8T2xVUykdjXimQkZKbMZB9Fk19ZtvNj1GDyvwfpPRi3xkd7KnY3ScZ8tlqmwJng6kS2m yIVvos047FseyLiThUd88UpdErshXQ1i7xhlj79QfzQjRJhwDz/fQJCSoiI2vy+r+iPD1K64c4cF kdk1aN3DouBSdI3sGtjUVXRkzzU+O1imtGci4dFU3FUewv6JO3nQzNsBu1jmkkAvwVTi4auWOLbJ Zih+zAZM061gDqv6j0syNxlTQzDIsDn/AG3xk3xjSiLrDLxM4m/XIIGwIdL6a1HqCVyei0kMlhXb gbrQe3f96HS/77Vbl3R3Gj8cL9kMqzJHtiwoXDtwbGAFkmCfBcJuYKcneGBstX3E6oQdUrrwWZNy wHIl'"
    a=SecurityMessageCrypto.MakeSecurityMessage('Newtouch-新致软件',pubkeypathB,prikeypathA,'123456','12345678901234')
    b=SecurityMessageCrypto.OpenSecurityMessage(a,pubkeypathA,prikeypathB,'123456')
    message=SecurityMessageCrypto.OpenSecurityMessage(cipher,pubkeypathA,prikeypathB,'123456')
    print(os.path.realpath(__file__))
    print(a)
    print(b)
    print(message)






