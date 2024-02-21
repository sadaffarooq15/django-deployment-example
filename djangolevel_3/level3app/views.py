from django import forms
from django.shortcuts import render
from .forms import FormName
# Create your views here.


def index(request):
    return render(request, 'app/index.html')

def form_name_view(request):
    form = FormName()
    
    if request.method =="POST":
        form = FormName(request.POST)   
        if form.is_valid():
             print("VALIDATION SUCESSS!!")
             print("NAME:" +form.cleaned_data['name'])
             print("EMAIL:" +form.cleaned_data['email'])
             print("TEXT:" +form.cleaned_data['text'])
    
    
    return render(request, 'app/formpage.html', {'form':form})
