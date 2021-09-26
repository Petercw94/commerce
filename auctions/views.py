from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from .forms import NewListingForm
from .models import User, Listing




def index(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "auctions/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def newListing(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewListingForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            # if the form is valid, save it to the database and return to the index page
            title = form.cleaned_data.get("title")
            description = form.cleaned_data.get("description")
            starting_bid = form.cleaned_data.get("starting_bid")
            image = form.cleaned_data.get("image")
            category = form.cleaned_data.get("category")
            user = request.user
            obj = Listing.objects.create(
                title = title,
                description = description,
                starting_bid = starting_bid,
                image = image,
                category = category,
                created_by = user
            )
            obj.save()            
            
            return HttpResponseRedirect("/")
        else:
            return render(request, 'auctions/newListing.html', {'form': form})
            
    # if a GET (or any other method) we'll create a blank form
    else:
        context = {
            'form': NewListingForm()
        }

        return render(request, 'auctions/newListing.html', context)


def listing(request, id):
    listing = Listing.objects.get(pk=id)
    return render(request, 'auctions/listing.html', {"listing":listing})