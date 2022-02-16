# from unicodedata import category
from django.http import HttpResponseRedirect
from django.shortcuts import render
from core.models import Contact_us, Category, Foodcard

# Create your views here.
# def main(request):
#     return render(request,'index.html')

def send(request):
    if request.method == 'POST':
        send = Contact_us()
        send.email = request.POST.get("email")
        send.save()
        return HttpResponseRedirect ('/')

def base(request):
    category= Category.objects.all()
    foodcard = Foodcard.objects.all()
    context ={'foodcard':foodcard, 'category':category}
    return render(request, 'index.html',context=context)