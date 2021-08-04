from django.shortcuts import render
from .models import Todo
# Create your views here.
def home(request):
	if request.method == 'POST':
		task=request.POST.get('task')
		print(task)
		new = Todo(task=task)
		new.save()
	return render(request,"main/form.html")
