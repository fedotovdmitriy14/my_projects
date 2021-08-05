from django.shortcuts import render
from django.views import View
from account.models import Account


class Menu(View):
    def get(self, request):
        accounts = Account.objects.all()
        return render(request, 'account/base.html', {'accounts': accounts})

    def post(self, request):
        name = request.POST.get('name')
        new = Account(name=name)
        new.save()
        return render(request, "account/base.html")


