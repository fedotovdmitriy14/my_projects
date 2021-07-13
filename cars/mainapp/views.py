from django.shortcuts import render


def menu(request):
    return render(request, 'mainapp/Mitsubishi_models.html')

# def show_main(request):
#     return render(request, 'mainapp/main.html')

def models(request):
    return render(request, 'mainapp/models.html')