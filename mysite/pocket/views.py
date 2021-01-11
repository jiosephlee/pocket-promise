from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import User,Organization
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import NewUserForm

def index(request):
    ordered_organization_list=Organization.objects.order_by(Lower('name').desc())
    context = {
        'ordered_organization_list': ordered_organization_list,
    }
    return render(request, 'pocket/index.html', context)

def detail(request, organization_id):
    organization = get_object_or_404(Organization, pk=organization_id)
    return render(request, 'pocket/detail.html', {'organization': organization})

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
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "main/login.html",
                    context={"form":form})
#https://pythonprogramming.net/user-login-logout-django-tutorial/
#this is the link of the login code i pulled
