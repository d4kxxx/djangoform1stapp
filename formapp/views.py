from django.shortcuts import render, redirect
from .models import UserForm
from formapp.userform import UserForms
from django.http import HttpResponse


# Create your views here.
def home(request):
    if request.method == "POST":
        myform = UserForms(request.POST)
        if myform.is_valid():
            name = myform.cleaned_data.get("name")
            phone = myform.cleaned_data.get("phone")
            email = myform.cleaned_data.get("email")
            address = myform.cleaned_data.get("address")
            data = UserForm(name=name, phone=phone, email=email, address=address)
            data.save()

    # else:
    #     return HttpResponse("HAHAHA")
    return render(request, "formapp/home.html", {"userform": UserForms})


def delete_event(request, event_id):
    event = UserForm.objects.get(pk=event_id)
    event.delete()
    return render(request, "formapp/home.html", {"userform": UserForms})


def details(request):
    all_data = UserForm.objects.all()
    return render(request, "formapp/details.html", {"items": all_data})
