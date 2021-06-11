from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt 

# Create your views here.

def index(request):
    return render(request, "index.html")

def home(request):
    if "user_id" not in request.session:
        return redirect('/')

    context = {
        "aisi_posts": AISI_Post.objects.all()
    }

    return render(request,"home.html", context)

def register(request):

    if request.method == "POST":

        errors = User.objects.validate(request.POST)
        if errors:
            for error in errors.values():
                messages.error(request,error)
            return redirect('/')


        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

        user = User.objects.create(first_name=first_name, last_name=last_name, username=username, email=email, password=pw_hash)

        request.session["user_id"] = user.id
        request.session["user_name"] = f"{username}"

        return redirect('/home')

    return redirect('/')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        logged_user = User.objects.filter(email=email)

        if logged_user:
            logged_user = logged_user[0]

            if bcrypt.checkpw(password.encode(), logged_user.password.encode()):
                request.session["user_id"] = logged_user.id
                request.session["user_name"] = f"{username}"
                return redirect('/home')
            else:
                messages.error(request,"Password is incorrect")

        else:
            messages.error(request,"This user doesn't exist")
            return redirect('/')

    return redirect('/')

def logout(request):
    request.session.flush()

    return redirect('/')


def partial(request,id):

    context = {
        "post": AISI_Post.objects.get(id=id)
    }

    return render(request,"partial.html",context) 

def partial_comment(request,id):

    context = {
        "comment": Comment.objects.get(id=id)
    }

    return render(request,"partial_comment.html",context)


def create_post(request):

    message = request.POST["message"] 

    poster = User.objects.get(id=request.session["user_id"])

    AISI_Post.objects.create(message=message,poster=poster)

    #aisi_post = AISI_Post.objects.create(message=message,poster=poster)

    return redirect('/home')
    #return redirect(f'/partial/{aisi_post.id}')


def add_comment(request,id):

    aisi_post = AISI_Post.objects.get(id=id)

    comment = request.POST["comment"]

    poster = User.objects.get(id=request.session["user_id"])

    Comment.objects.create(comment=comment,poster=poster,aisi_post=aisi_post)

    #new_comment = Comment.objects.create(comment=comment,poster=poster,AISI_Post=AISI_Post)

    return redirect('/home')
    #return redirect(f'/partial_comment/{new_comment.id}')

def like(request,id):

    aisi_post =  AISI_Post.objects.get(id=id)
    user = User.objects.get(id=request.session["user_id"])
    aisi_post.likes.add(user)

    return redirect('/home')
