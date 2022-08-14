from django.shortcuts import render,redirect

from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.models import User



def frontpage(request):
    return render(request,'core/front.html')


def SignUp(request):

    if request.method == "POST":
    
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.info(request, "Password Must Be The Same")
            return redirect('signup')
        elif User.objects.filter(username = username):
            messages.info(request, "User Exists")
            return redirect('signup')
        elif "@" not in username:
            messages.info(request, "Please Enter A Valid Email Address")
            return redirect('signup')
        
        else:
            hashedpwd = make_password(password)
            User.objects.create(username = username , password = hashedpwd ,email = username)
        
            messages.info(request, "You have been registered successfully now proceed to login")
            return redirect('login')
     

    return render(request, 'core/signup.html')# Create your views here.




def Signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        if User.objects.filter(username=username):
            user = authenticate(request,username = username , password = password)

            if user is not None:
                login(request, user)
                return redirect("signup")

            else:
                messages.info(request, "Incorrect Details" )
                return redirect("login")

        else:
            messages.info(request, "This User Does Not Exist" )
            return redirect("login")
    return render(request, 'core/login.html')


def Logout_view(request):

    logout(request)

    messages.info(request, "Thank You , You Have Logged Out Successfully" )
    return redirect("login")