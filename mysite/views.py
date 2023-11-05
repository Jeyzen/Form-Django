from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(requests):
    return HttpResponse(
        background_color="red",
        content="<h1>Hello World</h1>")