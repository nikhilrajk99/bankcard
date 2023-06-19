from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from credentials.forms import ApplicationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username):
                messages.info(request, "username is already taken")
                return redirect('register')
            else:
                User.objects.create_user(username=username, password=password)
                messages.info(request, "Registered Succesfully")
                return redirect('login')
        else:
            messages.info(request, "Password not match")
            return redirect('register')
    return render(request, "register.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            user.save()
            return redirect('form_page')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('register')
    return render(request, "login.html")


def form_page(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            # Logic to handle form submission
            # Replace this with your actual implementation
            form.save()
        return render(request, 'success.html', {'message': 'Application accepted'})
    else:
        form = ApplicationForm()

    return render(request, 'form.html',{'form': form})

def logout(request):
    auth.logout(request)
    return redirect('/')



