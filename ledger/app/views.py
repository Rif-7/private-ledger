from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
from .models import Categorie, User, Ledger
# Create your views here.

@login_required
def index(request):
    cats = Categorie.objects.filter(user=request.user).values_list("name", flat=True)
    return render(request, "app/index.html", {
        "cats": cats
    })


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "app/login.html", {
                "message": "Invalid username and/or password."
            })
    return render(request, "app/login.html", {
        "message": ""
    })


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["password2"]
        if password != confirmation:
            return render(request, "app/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            
        except IntegrityError:
            return render(request, "app/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "app/register.html")


@login_required
@csrf_exempt
def get_data(request):
    if request.method == "POST":
        transactions = Ledger.objects.filter(user=request.user).order_by("-date")
        cat = request.POST.get("categorie", False)
        print(cat)
        if cat:
            cat = "".join(cat.split(" "))
            cat = [c.capitalize() for c in cat.split(",")]
            transactions = transactions.filter(cat__in=cat)
        p_min = request.POST.get("min", False)
        if p_min:
            transactions = transactions.filter(amount__gte=p_min)
        p_max = request.POST.get("max", False)
        if p_max:
            transactions = transactions.filter(amount__lte=p_max)
        print(transactions.values_list("amount"))
        
        before = request.POST.get("before", False)
        if before:
            before = datetime.strptime(before, "%d/%m/%Y")
            print(before)
            transactions = transactions.filter(date__lte=before)

        after = request.POST.get("after", False)
        if after:
            print(after)
            after = datetime.strptime(after, "%d/%m/%Y")
            transactions = transactions.filter(date__gte=after)


        return JsonResponse([transaction.serialize() for transaction in transactions], safe=False)

    transactions = Ledger.objects.filter(user=request.user)
    transactions = transactions.order_by("-date").all()
    return JsonResponse([transaction.serialize() for transaction in transactions], safe=False)

@login_required
def add_new(request):
    if request.method == "POST":
        cat = request.POST['cat']
        dec = request.POST['description']
        amount = request.POST['amount']
        to = request.POST['to']

        if not cat or not dec or not amount or not to:
            return HttpResponse("Input all the data")
        usr_cats = request.user.cats.filter(name=cat.capitalize())
        Ledger(user=request.user, cat=cat.capitalize(), description=dec, amount=amount, to=to).save()
        if not usr_cats:
            Categorie(user=request.user, name=cat.capitalize()).save()
        
    return HttpResponseRedirect(reverse("index"))


@login_required
def stats(request):
    cats = Categorie.objects.filter(user=request.user).values_list("name", flat=True)
    totals = []
    i = 0
    for cat in cats:
        i += 1
        totals.append({"cat": cat,
                    "amount": sum(Ledger.objects.filter(user=request.user, cat=cat).values_list("amount", flat=True))
                    })

    totals = [a for a in sorted(totals, key=lambda x: x["amount"])]
    totals.reverse()
    return JsonResponse(totals, safe=False)