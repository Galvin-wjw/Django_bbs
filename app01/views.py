from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def index(request):
    return render(request,'index.html')
@login_required
def host(request):
    return render(request,'host.html')
@login_required
def audit(request):
    return render(request,'audit.html')
@login_required
def asset(requset):
    return render(requset,'asset.html')

def acc_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        user = authenticate(username = username,password = passwd)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
        else:
            return render(request,'login.html',{
                'login_err':'Wrong user or password'
            })
    else:

        return render(request,'login.html')

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/')