from django.shortcuts import render

# Create your views here.

#teste
def home_view(request, *args, **kwargs):
	context = {}
	return render(request, "home.html", context)

def contact_view(request, *args, **kwargs):
	return render(request, "contact_form.html", {})


#a ser utilizadas
def index_view(request, *args, **kwargs):
	context = {}
	return render(request, "index.html", context)

def about_view(request, *args, **kwargs):
	context = {}
	return render(request, "about.html", context)

def code_view(request, *args, **kwargs):
	context = {}
	return render(request, "code.html", context)

def solutions_view(request, *args, **kwargs):
	context = {}
	return render(request, "solutions.html", context)

def faq_view(request, *args, **kwargs):
	context = {}
	return render(request, "FAQ.html", context)
