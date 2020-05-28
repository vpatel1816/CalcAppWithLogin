from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('psw')
        password2 = request.POST.get('psw2')
        print('done')
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username has been taken')
                return render(request,'accounts/register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email has been taken')
                return render(request, 'accounts/register.html')
            else:
                Data = User.objects.create_user(username=username, email=email, password=password)
                Data.save()
                messages.info(request, 'Account has been created')
                return render(request, 'accounts/login.html')
        else:
            messages.info(request,'Passwords are not same, please try again')
            return render(request, 'accounts/register.html')
    else:
        return render(request,'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('psw')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/calculator')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request,'accounts/login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')