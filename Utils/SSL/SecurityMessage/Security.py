from SecurityMessage import A
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
        return A.decrypt(cipher,pubkeypath,prikeypath,pwd)

    @classmethod
    def MakeSecurityMessage(cls,message,pubkeypath,prikeypath,pwd,shopId):
        paramString=cls.shop(shopId)
        return paramString+A.encrypt(message,pubkeypath,prikeypath,pwd)










