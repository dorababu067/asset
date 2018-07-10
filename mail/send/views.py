from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(requst,*args,**kwargs):
    if requst.method == 'POST':
        print(args,kwargs)
        email = requst.POST['email']
        passw = requst.POST['psw']
        repass = requst.POST['psw-repeat']

        send_mail("confirmation",
        "this is send by dorababujfdsadjafksdhfkjhaskjhfdskhfkajhdskjfhjkahj",
        "dorababua77@gmail.com",
        [email])
        return HttpResponse("<h1>sent.............</>")
    else:
       return render(requst,"index.html",{}) 