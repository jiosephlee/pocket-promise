from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import User,Organization
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import NewUserForm

def index(request):
    ordered_organization_list=Organization.objects.order_by('name')
    context = {
        'ordered_organization_list': ordered_organization_list,
    }
    return render(request, 'pocket/index.html', context)

def detail(request, organization_id):
    organization = get_object_or_404(Organization, pk=organization_id)
    return render(request, 'pocket/detail.html', {'organization': organization})

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("pocket:index")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request = request,
                          template_name = "pocket/register.html",
                          context={"form":form})

    form = NewUserForm
    return render(request = request,
                  template_name = "pocket/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("pocket:index")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('pocket:profile', args=(user.id,)))
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "pocket/login.html",
                    context={"form":form})


def profile(request,user_id):
    response = "You're looking at the profile of user %s."
    return HttpResponse(response % user_id)
#https://pythonprogramming.net/user-login-logout-django-tutorial/
#this is the link of the login code i pulled
