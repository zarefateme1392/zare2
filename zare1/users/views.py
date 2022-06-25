from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
#from users.forms import UserAdminCreationForm
from .forms import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .utils import send_sms
import numpy as np
import time
from users.models import CustomUser
from rest_framework.decorators import action
###################################################################################### API
@api_view(['GET'])
def getusers(request):
    user=CustomUser.objects.all()
    serializer=UserSerializer(user,many=True)
    return Response(serializer.data)
"""
@api_view(['POST'])
def signup(request):
    data=request.data
    phonenumber=data['phonenumber']
    global phonenumber1, code1
    phonenumber1 = phonenumber
    if len(phonenumber)>11 or len(phonenumber)<11:
        return Response("باید 11 رقمی باشد")
    elif not phonenumber.isnumeric():
        return Response("شماره باید عددی باشد")
    elif  phonenumber[1]!='9':
        return Response("عدد دوم باید 9 باشد")

    code1 = np.random.randint(100000, 999999)
    print('code2 in register', code1)
    print("phoneeeeeeeeeeeeee", phonenumber1)
    send_sms(code1, phonenumber1)
    return Response("sms send")
        #else:
        #return redirect("signup")



"""
@api_view(['POST'])
def signinorup(request):
    data = request.data
    phonenumber=data['phonenumber']
    print("pn",phonenumber)
    if not phonenumber.isnumeric():
        content = {'باید عددی باشد'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    elif len(phonenumber)>11 or len(phonenumber)<11:
        content = {'باید حتما 11 رقمی باشد'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    elif phonenumber[1]!='9':
        content = {'عدد دوم باید حتما 9 باشد'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    user = CustomUser.objects.filter(phonenumber=phonenumber)
    print("userrrrrrrrrrrrrrrrrrrrrrrrrrrrrr", user)
    if user:
        print("if")
        user = CustomUser.objects.get(phonenumber=phonenumber)
        code = Code.objects.get(user=user)
        code.time1=time.time()
        print("time1",code.time1)
        code.save()
        print("codeeeeeeeeeeeeee", code)
        send_sms(code, phonenumber)
        request.session['pk'] = user.pk
        return Response('send login')

    else:
        print("else")
        user = CustomUser.objects.create(phonenumber=phonenumber, is_active=False)
        code = Code.objects.get(user=user)
        print(user)
        print(code)
        send_sms(code, phonenumber)
        request.session['pk'] = user.pk
        return Response('send register')

"""
@api_view(['POST'])
def codeserializer(request):

    data = request.data
    num=data['number']
    print('num vared shode in verify', num)
    if np.str(code1) == num:
        print("yeeeeeeeeeeeeeeeeeeeeeeeees")
        user = CustomUser.objects.create(phonenumber=phonenumber1)
        user.is_active = True
        return Response('this is register')
    else:
        return Response('error')

"""
@api_view(['POST'])
def codeserializer1(request):
    pk = request.session.get('pk')
    print("pkkkkkkkkkkkkkkkk", pk)
    if pk:
        user = CustomUser.objects.get(pk=pk)
        code = user.code
        pn=user.phonenumber
        print("pnnnnnnnnnnnnnnnnnnnn",pn)
        data = request.data
        num=data['number']
        print('num vared shode in verify', num)
        code.time2 = time.time()
        #code.save()
        print("time2",code.time2)
        dif=code.time2-code.time1
        print("dif",dif,type(dif))
        print("code bad dif",user.code)
        if dif<120:
            if np.str(code) == num:

                print("yeeeeeeeeeeeeeeeeeeeeeeeees")
                code.save()
                if user.is_active == True:
                    print("login")
                    login(request, user)
                    print("userrrr", user)
                    return Response('login')
                else:
                    user.is_active = True
                    user.save()
                # login(request, user)
                # print("userrrr", user)
                    print("register")
                    return Response('register')
            else:
                content = {'NOT VARIFY'}
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)
        else:
            print("to difffffffffffff")
            content = {'NOT VARIFY'}
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)



    else:
        content = {'not found'}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
        #return Response('error')


################################################################################
"""
def verifysugnup(request):
    data1= codeserializer(request)

    if data1:
        num = data1
        print('num vared shode in verify', num)
        if np.str(code2) == num:
            print("yeeeeeeeeeeeeeeeeeeeeeeeees")
            user = CustomUser.objects.create(phonenumber=phonenumber1)
            user.is_active=True
            return HttpResponse('this is register')
        else:
            return redirect('signup')

    #return render(request, 'verify.html', {'form': form})
"""

class UserViewSet(viewsets.ModelViewSet):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    #print(serializer_class)

    @action(detail=True, methods=['POST'])
    def set_phonenumber(self, request, pk=None):
        print("yessssssssssssssssssssss")
        user = self.get_object()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user.phonenumber(serializer.validated_data['phonenumber'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)