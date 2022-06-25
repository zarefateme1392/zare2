import ghasedakpack
import numpy as np

def send_sms(code_user,phonenumber):
    code=np.str(code_user)
    print(code,type(code))
    pn=np.str(phonenumber)
    print(pn)
    sms = ghasedakpack.Ghasedak("2e472b7a78524990250224f42b25770d20ef3b9a802046c46b58397f69ba8f0e")
    sms.send({'message': code, 'receptor': pn, 'linenumber': '10008566'})
    print("send")


    #import ghasedak
    #message = "تست ارسال وب سرویس قاصدک"
    #receptor = "09138884751"
    #linenumber = "10008566"
    #sms = ghasedak.Ghasedak("2e472b7a78524990250224f42b25770d20ef3b9a802046c46b58397f69ba8f0e")
    #sms.send({
      #  'message': message,
       # 'receptor' : receptor,
       # 'linenumber': linenumber
       # })