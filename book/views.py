from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import auth,User

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated == False :
        return redirect ('login')
    else:
        return render (request, 'index.html')

    
def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        new_user=User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        new_user.save()
        return HttpResponse('data save')
    else:   
        return render (request, 'signup.html')





def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
           
        else:
            return HttpResponse('password wrong')
    else:
        return render (request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')



