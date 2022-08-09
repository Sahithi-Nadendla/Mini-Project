from django.shortcuts import render
from django.http import HttpResponse
from django import forms
import spacy

nlp = spacy.load("C:\MiniProject\VirtualChatbotForLibrary\LibraryAssistant\output\model-best")

class user_input(forms.Form):
    u_input=forms.CharField(label="")

# Create your views here.
def index(request):
    if request.method=="POST":
        form=user_input(request.POST)
        if form.is_valid():
            doc = nlp(form.cleaned_data["u_input"])
            for ent in doc.ents:
                print(ent.text,ent.label_,"---------------------------------------------------------")
        
    return render(request,"LibraryAssistant/index.html",{"form":user_input()})