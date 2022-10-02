from importlib.resources import contents
import re
from django.shortcuts import render, redirect
from .models import Review, User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    k = Review.objects.all()
    context = {"c": k}
    return render(request, "Pair1/index.html", context)


def home(request):
    k = Review.objects.all()
    return redirect("Pair1:index")


def index1(request, pk):
    k = Review.objects.all()
    return redirect("Pair1:index")


def new(request):
    return render(request, "Pair1/new.html")


def create(request):
    k = request.GET
    v = [k[i] for i in k]
    Review.objects.create(title=v[0], content=v[1])
    return redirect("Pair1:index")


def detail(request, pk):
    k = Review.objects.get(pk=pk)
    context = {"c": k}
    return render(request, "Pair1/detail.html", context)
def details(request):
    k = Review.objects.latest('pk')
    context = {
        "c":k
    }
    return render(request,"Pair1/details.html",context)

def delete(request, pk):
    Review.objects.get(pk=pk).delete()
    return redirect("Pair1:index")


def edit(request, pk):
    k = Review.objects.get(pk=pk)
    context = {"c": k}
    return render(request, "Pair1/edit.html", context)


def update(request, pk):
    r = Review.objects.get(pk=pk)

    title = request.GET.get("title")
    content = request.GET.get("content")

    r.title = title
    r.content = content

    r.save()
    return redirect("Pair1:detail", r.pk)
@csrf_exempt
def logins(request):
    if request.method == "GET":
        return render(request, 'Pair1/Users.html')
@csrf_exempt
def Users(request):
    if request.method == "GET":
        return render(request, 'Pair1/Users.html')
    elif request.method == "POST":
        user_id = request.POST.get('id', '')
        user_pw = request.POST.get('pw', '')
        user_pw_confirm = request.POST.get('pw-confirm', '')
        user_name = request.POST.get('name', '')
        user_email = request.POST.get('email', '')

        if (user_id or user_pw or user_pw_confirm or user_name or user_email) == "":
            return redirect('/Pair1/Users')
        elif user_pw != user_pw_confirm:
            return redirect('/Pair1/Users')
        else:
            user = User(
                user_id = user_id,
                user_pw = user_pw,
                user_name = user_name,
                user_email = user_email
            )
            user.save()
        return redirect('/')