from django.shortcuts import render
from django.http import HttpResponse
from .import forms

# Create your views here.
def homepage(request):
	return render(request, 'myapp/homepage.html')

def about(request):
	return render(request, 'myapp/about.html')

def gallery(request):
	return render(request, 'myapp/gallery.html')

def signin(request):
	return render(request, 'myapp/signin.html')

def signup(request):
	return render(request, 'myapp/signup.html')

def contact(request):
	return HttpResponse(" Hi, This is contact page")

def custom(request):
	dict_var = {'balu_template':'Used to display custom webpage'}
	return render(request, 'myapp/login.html', context= dict_var)

def login_form(request):
	form = forms.FormName()
	if request.method == "POST":
		form = forms.FormName(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'myapp/login.html', {'login_form':form})