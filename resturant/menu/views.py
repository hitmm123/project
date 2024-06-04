from tkinter import Menu

from django.shortcuts import render, redirect, reverse
from django import forms
from django.core.exceptions import ValidationError
from .models import Deliveryi
from .forms import MenuForm
#foodlist = []
#BRANCH = [(1, "khrebat al-souq"), (2, "yadoudeh"), (3, "zezia"), (4, "madaba")]
#delivery = []


#def validate_name(value):
 #   if len(value.split(" ")) < 2:
  #      raise ValidationError("must be two words")


#class Deliveryinfo(forms.Form):
 #   id = forms.IntegerField(required=True, max_value=99999, label="your phone")
  #  adress = forms.CharField(max_length=200, required=True, label="your address")
   # name = forms.CharField(max_length=200, required=True, label="your name", validators=[validate_name])
    #branch = forms.ChoiceField(choices=BRANCH)
    #password = forms.CharField(widget=forms.PasswordInput)


#def index(request):
 #   return render(request, "index.html",
  #                context={'foods': list(enumerate(foodlist)), 'pass': True})
def index(request):
    if request.method=="POST":
        if "delete" in request.POST:
            bid=request.POST['delete']
            Deliveryi.objects.get(pk=bid).delete()

    food_list=Deliveryi.objects.all().order_by("name")
    return render(request, "index.html",
                  context={'foods': food_list})


def add(request):
    if request.method == 'POST':
        #b2 = Deliveryinfo(request.POST)
        b2=MenuForm(request.POST)
        if b2.is_valid():
            #foodlist.append(request.POST)
            b2.save()
            return redirect(reverse("menu:homepage"))
        else:
            return render(request, "add.html", context={'deli': b2})
   # d = Deliveryinfo()
    d = MenuForm()
    return render(request, "add.html", context={'deli': d})




    return render(request, "add.html", {'deli_form': form})
def delete(request, pos):
    return redirect(reverse("menu:homepage"))
   # Deliveryi.pop(pos)
