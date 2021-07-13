from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm
import random

from .models import User

# Create your views here.
from rest_framework.views import APIView

#
# class UserAPI(APIView):
    # def get(self, request):                 # чтобы вывести джанго форму, нужно связать ее с вьюхой
    #     form = UserForm                     # 1
    #     data = {                            #2
    #         'form': form
    #     }
    #     return render(request, "articles/main_page.html", data)         #3
    #
    #
    # def post(self, request):
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         name = form.cleaned_data['login']
    #         psw = form.cleaned_data['user_psw']
    #         user = User.objects.filter(login=name, user_psw=psw)
    #
    #         if user:
    #             user.token = random.randint(0, 100000)
    #             print(user.token)
    #             return HttpResponse("Awesome")
    #
    #         else:
    #             return HttpResponse("Not even close")

class UserAPI(APIView):
    def get(self, request):



