from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import RegisterUserForm, LoginUserForm, RegisterBookForm
from .models import Book

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def form_register(request):
    if request.method == 'POST':
        val_form = RegisterUserForm(request.POST)
       
        if val_form.is_valid():
            val_form.save() 
        else:
            print(val_form.errors)
            return HttpResponse(val_form.errors)

    val_form = RegisterUserForm()
    return render(request,'account/home.html',{'form_register': val_form})

def form_login(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # return render(request,'account/register_book.html')
            return redirect('register_book')

        return HttpResponse("Wrong Credentials or the user doesn't exist.")

    form = LoginUserForm()
    return render(request,'account/login.html',{'form_login': form})

@login_required(login_url='account:form_login')
def log_out(request):
    logout(request)
    return HttpResponse("Logged out successfully.")

@login_required(login_url='account:form_login')
def register_book(request):
    if request.method == 'POST':
        form = RegisterBookForm(request.POST)

        if form.is_valid():
            form.save()
            form_empty = RegisterBookForm()
            return render(request,'account/register_book.html',{'register_book': form_empty})
        else:
            return render(request,'account/register_book.html',{'register_book': form})

    form = RegisterBookForm()
    data = Book.objects.order_by('-id')[:5]
    return render(request,'account/register_book.html',{'register_book': form, 'data_set' : data})
