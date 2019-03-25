from django.shortcuts import render,redirect
import datetime as dt
from django.http  import HttpResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .forms import *

def index(request):
    date = dt.date.today()
    hoods = Hood.objects.all()
    return render(request, 'index.html',{"date":date, "hoods":hoods})


def profile(request):
    date = dt.date.today()
    current_user = request.user
    profile = UserProfile.objects.get(user=current_user.id)
    hoods = Hood.objects.all()
    return render(request, 'profile/profile.html', {"date": date, "profile":profile,"hoods":hoods})

def edit_profile(request):
    date = dt.date.today()
    current_user = request.user
    profile = UserProfile.objects.get(user=current_user.id)
    if request.method == 'POST':
        signup_form = UpdateProfileForm(request.POST, request.FILES,instance=request.user.profile)
        if signup_form.is_valid():
            signup_form.save()
            return redirect('profile')
    else:
        signup_form =UpdateProfileForm()

    return render(request, 'profile/edit_profile.html', {"date": date, "form":signup_form,"profile":profile})
@login_required(login_url='/accounts/login/')
def new_hood(request):
    current_user = request.user
    profile = UserProfile.objects.get(user=current_user)
    if request.method == 'POST':
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user = current_user
            hood.profile = profile
            hood.save()
        return redirect('index')
    else:
        form = HoodForm()
    return render(request, 'new_hood.html', {"form": form})
def new_post(request,id):
    date = dt.date.today()
    hoody=Hood.objects.get(id=id)
    posts = Post.objects.filter(hood=hoody)
    comments = Comment.objects.filter(post=id).order_by('-pub_date')

    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.profile = profile
            post.hood = hoody
            post.save()
            return redirect('index')
    else:
        form = PostForm()
        return render(request,'new_post.html',{"form":form,"posts":posts,"hoody":hoody,  "date":date, 'comments':comments})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.objects.filter(name=search_term)
        message = f"{search_term}"
        profiles=  UserProfile.objects.all( )

        return render(request, 'search.html',{"message":message,"business": searched_businesses,'profiles':profiles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})


def location(request):
    date = dt.date.today()
    return render(request, 'location.html',{"date":date})


def newcomment(request,id):
    current_user = request.user

    try:
        comments = Comment.objects.filter(post_id=id)
    except:
        comments = []
    brush= Post.objects.get(id=id)
    if request.method =="POST":
        form = NewCommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.postername = current_user
            comment.post = brush
            comment.save()
    else:
        form = NewCommentForm()

    return render(request, 'newcomment.html',{'brush':brush,"comments":comments,"form":form})

def post_business(request,id):
    date = dt.date.today()
    hood=Hood.objects.get(id=id)
    business = Business.objects.filter(business_hood=hood)
    form = AddBusinessForm()
    if request.method == 'POST':
        form = AddBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.profile = request.user.profile
            business.hood = hood
            business.save()
            return redirect('index')
    else:
        form = AddBusinessForm()
        return render(request,'new_business.html',{"form":form,"business":business,"hood":hood,  "date":date})

@login_required(login_url='/accounts/login/')
def hood(request,id):
    current_user=request.user
    date = dt.date.today()
    post=Hood.objects.get(id=id)

    brushs = Post.objects.filter(post_hood=post)
    business = Business.objects.filter(business_hood=post)
    return render(request,'each_neighood.html',{"post":post,"date":date,"brushs":brushs, "business":business})



def signout(request):
    logout(request)
    return redirect('login')