from django.shortcuts import render, redirect
from django.views import View
from rest_framework.views import APIView

from account.forms import AccountForm
from account.models import Account


# def home(request):
#     if request.method == 'POST':
#         task=request.POST.get('task')
#         print(task)
#         new = Account(task=task)
#         new.save()
#     return render(request,"account/base.html")


class MenuAPI(View):
    def get(self, request):
        accounts = Account.objects.all()
        # form = AccountForm
        return render(request, 'account/base.html', {'accounts': accounts})

    def post(self, request):
        name = request.POST.get('name')
        print(name)
        new = Account(name=name)
        new.save()
        return render(request, "account/base.html")

        # form = AccountForm(request.POST)
        # error = ''
        # if form.is_valid():
        #     instance = form.save(commit=False)
        #     instance.user = request.user
        #     instance.save()
        #     # return redirect('menu', permanent=True)
        # else:
        #     error = 'Ошибка. Проверьте, правильно ли заполнены поля'
        #
        # form = AccountForm()
        #
        # data = {
        #     'form': form,
        #     'error': error
        # }
        # return render(request, 'accounts/base.html', data)

