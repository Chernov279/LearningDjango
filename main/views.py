from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {
        "title": "Home Page",
        "content": "You\'re at home!"
    }
    return render(request=request, template_name="main/index.html", context=context)