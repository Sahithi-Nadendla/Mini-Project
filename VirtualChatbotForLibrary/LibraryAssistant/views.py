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







#2 commit
#from pickle import NONE
from concurrent.futures.thread import BrokenThreadPool
from logging import PlaceHolder
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import BooksLocations,BooksDetails
#from django.core.mail import send_mail

import spacy

nlp = spacy.load("C:\MiniProject\VirtualChatbotForLibrary\LibraryAssistant\output\model-best")

class user_input(forms.Form):
    u_input=forms.CharField(widget=forms.TextInput(attrs={'class': 'bar','placeholder':"Search by Title,Author,Publication etc...."}))

def obtain_details(query_set):
    arr_list=[]
    query_set=query_set.order_by('popularity_rating')[0:5]
    for book in query_set:
        x=book.rack_number
        print(str(x)+"*88888888888888888888888888888888888888888888888888888888888888s")
        locations=BooksLocations.objects.get(from_rack_number__lte=x,to_rack_number__gte=x)
        arr_list.append(book.title+" by "+book.author+" is located in rack number "+str(x)+" which is in the "+locations.location+".")
    return arr_list

# Create your views here.
def index(request):
    if request.method=="POST":
        form=user_input(request.POST)
        if form.is_valid():
            author=[]
            title=None
            publication=None
            #subjects=[]
            inp=form.cleaned_data["u_input"]
            doc = nlp(inp)
            for ent in doc.ents:
                st=ent.text
                entity=ent.label_
                if entity=="WORK_OF_ART":
                    title=st.upper()
                elif entity=="PERSON":
                    author.append(st.upper())
                else:
                    publication=st.upper()
                print(st,entity,"-----------------------------------------------------------------")
            details=BooksDetails.objects.all()
            '''if title!=None:
                details=details.filter(title__contains=title,availability_status=True)
            if author!=None:
                details=details.filter(author__contains=author,availability_status=True)
            if publication!=None:
                details=details.filter(publisher__contains=publication,availability_status=True)
            print(title,author,publication,details.count())
            bot_response=""
            l=[]
            if(details.count()==0):
                bot_response="Not available"
            else:
                details=details.order_by('popularity_rating')[0:5]
                for book in details:
                    x=book.rack_number
                    print(str(x)+"*88888888888888888888888888888888888888888888888888888888888888s")
                    locations=BooksLocations.objects.get(from_rack_number__lte=x,to_rack_number__gte=x)
                    l.append(book.title+" by "+book.author+" is located in rack number "+str(x)+" which is in the "+locations.location+".")
                bot_response="Available"
                print(l)'''
            qs=[None,None,None,None]
            if title!=None:
                qs_t=details.filter(title__contains=title,availability_status=True)
                if qs_t.count()!=0:
                    qs[0]=qs_t
                qs_s=details.filter(subject__contains=title,availability_status=True)
                if qs_s.count()!=0:
                    qs[1]=qs_s
            if author!=[]:
                qs_a=details.filter(author__contains=author[0],availability_status=True)
                for i in author[1:]:
                    qs_a=qs_a | details.filter(author__contains=i,availability_status=True)
                if qs_a.count()!=0:
                    qs[2]=qs_a
            if publication!=None:
                qs_p=details.filter(publisher__contains=publication,availability_status=True)
                if qs_p.count()!=0:
                    qs[3]=qs_p
            print(title,author,publication)
            l=[]
            if qs[0]!=None:
                l.append("Available")
                l.extend(obtain_details(qs[0]))
            if qs[1]!=None or qs[2]!=None or qs[3]!=None :
                l.append("Here are some recommendations :")
                if qs[1]!=None:
                    l.append("Based on Subject :")
                    l.extend(obtain_details(qs[1]))
                if qs[2]!=None:
                    if qs[1]!=None:
                        qs[2]=qs[2].difference(qs[1])
                    l.append("Based on Author :")
                    l.extend(obtain_details(qs[2]))
                if qs[3]!=None:
                    if qs[1]!=None:
                        if qs[2]!=None:
                            qs[3]=qs[3].difference(qs[1],qs[2])
                        else:
                            qs[3]=qs[3].difference(qs[1])
                    elif qs[2]!=None:
                        qs[3]=qs[3].difference(qs[2])
                    l.append("Based on Publisher :")
                    l.extend(obtain_details(qs[3]))
            else:
                l.append("Not available")
            print(l)
            #send_mail('Subject here','Here is the message.','nadendla.sahithi231101@gmail.com',['medishettyvaishnavi396@gmail.com','nadendla.sahithi231101@gmail.com'],fail_silently=False,)
            return render(request,"LibraryAssistant/index.html",{"l":l,"form":user_input()})
    return render(request,"LibraryAssistant/index.html",{"form":user_input()})
