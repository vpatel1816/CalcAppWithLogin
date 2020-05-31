from django.shortcuts import render
from .models import ContactInfo


# Create your views here.
def home(request):
    return render(request,'fapp/home.html')

def contact(request):
    if request.method == "POST":
        fn = request.POST.get('fn')
        ln = request.POST.get('ln')
        subject = request.POST.get('subject')
        c = ContactInfo(fn=fn,ln=ln,subject=subject)
        c.save()
        return render(request,'fapp/contact_us.html')
    else:
        return render(request, 'fapp/contact_us.html')

def calculator(request):
    if request.method == "POST":
        fn = int(request.POST.get('fv'))
        sv = int(request.POST.get('sv'))
        v = fn + sv
        return render(request, 'fapp/calculator.html',{'v':v})
    else:
        return render(request, 'fapp/calculator.html')

def about(request):
    return render(request, 'fapp/about.html')

