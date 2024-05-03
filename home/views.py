from django.shortcuts import redirect, render
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import Visitor
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


# General Function Based Views
# def home(request):
#     return render(request, "home/welcome.html", {"today": datetime.today()})

# Class Based View of HOME
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {"today": datetime.today()}

# @login_required(login_url="/admin")
# def authorized(request):
#     return render(request, "home/authorized.html")

# Class Based View of Authorized
class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'


class UserRegisterationSuccess(TemplateView):
    template_name ='home/success_page.html'

class VisitorRegisterationForm(TemplateView):
    template_name = 'home/register_visitor.html'

def register_visitor(request):
    if request.method == "POST":
        userName = request.POST.get("userName")
        firstName = request.POST.get("firstName")
        middleName = request.POST.get("middleName")
        lastName = request.POST.get("lastName")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        email = request.POST.get("email")
        phoneNumber = request.POST.get("phoneNumber")
        password = request.POST.get("password")
        confirmPassword = request.POST.get("confirmPassword")

        if password != confirmPassword:
            return render(
                request,
                "home/register_visitor.html",
                {"error": "Password do not match"},
            )

        Visitor.objects.create(
            userName=userName,
            firstName=firstName,
            middleName=middleName,
            lastName=lastName,
            email=email,
            address=address,
            phoneNumber=phoneNumber,
            gender=gender,
            password=password,
            confirmPassword=confirmPassword,
        )
        return redirect("home/success_page.html")
    return render(request, "home/register_visitor.html")


# Class Based Views
# class
