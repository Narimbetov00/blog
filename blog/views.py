from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,logout
from . import forms,models
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def homepage(request):
    posts = models.Blog.objects.all()
    return render(request,'home.html',{'posts':posts})

def post_detail(request,id):
    post = get_object_or_404(models.Blog,id=id)
    return render(request,'post_detail.html',{'post':post})
def registration(request):
    if request.method == 'POST':
        form = forms.RegistionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return   redirect('homepage')
    else:
        form = forms.RegistionForm()
    return render(request,'registration.html',{'form':form})


def loginpage(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('homepage')
    else:
        form = forms.AuthenticationForm()
    return render(request,'login.html',{'form':form})


def logoutpage(request):
    logout(request)
    return redirect('homepage')


def create_post(request):
    if request.method == 'POST':
        form = forms.BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = forms.BlogForm()
    return render(request,'create_post.html',{'form':form})