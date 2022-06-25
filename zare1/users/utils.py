import ghasedakpack
import numpy as np
from kavenegar import *
def send_sms(code_user,phonenumber):
    print("***************************************")
    code=np.str(code_user)
    print(code)
    pn=np.str(phonenumber)
    print(pn)
    sms = ghasedakpack.Ghasedak("48a5a1d8df60c5617d0dfadfd1fe5f46782b793a04fc245ba5c4c769fab56002")
    sms.send({'message': code, 'receptor': pn, 'linenumber': '10008566'})
    print("send")
    #api = KavenegarAPI('36446B5531747642656C6E5150785A46382B3538676F50595866506E4D4771577175732B51666245696C633D')
    #params = {
        #'sender': '10004346',
       # 'receptor': pn,
       # 'message': code
    #}
   # response = api.sms_send(params)
    """
    try:
        api = KavenegarAPI('36446B5531747642656C6E5150785A46382B3538676F50595866506E4D4771577175732B51666245696C633D')
        params = {
            'sender': '10004346',
            'receptor': pn , # multiple mobile number, split by comma
            'message': code,
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
   # print("send")
   """
    """
    try:
        import json
    except ImportError:
        import simplejson as json
    try:
        print("try")
        api = KavenegarAPI('36446B5531747642656C6E5150785A46382B3538676F50595866506E4D4771577175732B51666245696C633D')
        print("api",api)
        params = {
            'sender': '10004346',
            'receptor': pn,
            'message': code
        }
        print(params)
        response = api.sms_send(params)
        print("rrrrrrrrrrrrrrr",response)
        print("response",np.str(response))

    except APIException as e:
        print("1111111111")
    except HTTPException as e:
        print("2222222222222222")
        """



    #api = KavenegarAPI('417061753268423371486F512B7078573343716D5A514143354B53504C4D64784C6E4D38684463767578553D')
    #params = {'sender': '100047778', 'receptor': pn, 'message':code}
    #send= api.sms_send(params)
    #print("sendddddddddddddddddddddddddd")
   # print(send)





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