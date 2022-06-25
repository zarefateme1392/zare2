from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from codes.forms import CodeForm
from users.forms import RegisterForm
from users.models import CustomUser
from django.http import HttpResponse
import numpy as np
from .utils import send_sms
from codes.models import Code



@login_required
def home_view(request):
    return render(request,'main.html',{})

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        #username = request.POST.get('username')
        #password = request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')
        print(phonenumber)
        if form.is_valid():
            user=CustomUser.objects.filter(phonenumber=phonenumber)
            print("userrrrrrrrrrrrrrrrrrrrrrrrrrrrrr",user)
            if user:
                print("if")
                user = CustomUser.objects.get(phonenumber=phonenumber)
                code = Code.objects.get(user=user)
                print("codeeeeeeeeeeeeee",code)
                send_sms(code, phonenumber)
                request.session['pk'] = user.pk
                return redirect('verify-view')

            else:
                print("else")
                user = CustomUser.objects.create(phonenumber=phonenumber, is_active=False)
                code = Code.objects.get(user=user)
                print(user)
                print(code)
                send_sms(code, phonenumber)
                request.session['pk'] = user.pk
                return redirect('verify-view')

    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
#############################################################################################

def auth_view(request):
    form = AuthenticationForm()
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            request.session['pk']=user.pk
            return redirect('verify-view')

    return render(request,'auth.html',{'form':form})


def verify_view(request):
    form=CodeForm(request.POST or None)
    pk=request.session.get('pk')
    print("pkkkkkkkkkkkkkkkk",pk)
    if pk:
        user=CustomUser.objects.get(pk=pk)
        code=user.code
        code_user=f"{user.username}:{user.code}"
        #if not request.POST:
            #print(code_user)
            #print("phoneeeeeeeeeeeeee",user.phonenumber)
            #send_sms(code_user,user.phonenumber)
        if form.is_valid():
            cd=form.cleaned_data
            print(cd)
            num=cd['number']
            print('num',num)
            if np.str(code)==num:
                print("yeeeeeeeeeeeeeeeeeeeeeeeees")
                code.save()
                if user.is_active==True:
                    print("login")
                    login(request,user)
                    print("userrrr",user)
                    return render(request,'main.html',{'user':user})
                else:

                    user.is_active=True
                    user.save()
                    #login(request, user)
                   # print("userrrr", user)
                    print("register")
                    return render(request, 'main.html', {'user': user})
                    #return HttpResponse("it is register")
            else:
                return redirect('login-view')
    return render(request,'verify.html',{'form':form})







