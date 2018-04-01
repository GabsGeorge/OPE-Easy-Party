from django.shortcuts import render
from core.models import Produto

def index(request):
	return render(request, "index.html")		

def Produto(request):
	contexto = {
		"produtos":Produto.objects.all()
	}
	return render(request,"index.html", contexto)

# Create your views here.
