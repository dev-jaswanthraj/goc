from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import HttpResponse
from home.models import contact_us,  prayer_request

# Create your views here.
@login_required(login_url='/loginPage')
def home(request):
    context_a = [] 
    context_a1 = []
    context_b = [] 
    context_b1 = []
    context_c = []
    context_c1 = []
    user = temp_reg.objects.all()
    per_user = permanent_reg.objects.all()
    for i in user:
        if  i.user_type == 'BUYER':
            context_a.append(i)
        elif i.user_type == 'DONATION':
            context_b.append(i)
        else:
            context_c.append(i)
    for i in per_user:
        if  i.user_type == 'BUYER':
            context_a1.append(i)
        elif i.user_type == 'DONATION':
            context_b1.append(i)
        else:
            context_c1.append(i)
    context={
        'context_a':context_a,
        'context_b':context_b,
        'context_c':context_c,
        'context_a1':context_a1,
        'context_b1':context_b1,
        'context_c1':context_c1,
        }
    return render(request, "status.html",context)

def loginPage(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/admin1")
            
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/')

def add(request,id):
    val = temp_reg.objects.get(id = id)
    first_name = val.first_name 
    last_name = val.last_name
    phone_number = val.phone_number 
    building_name = val.building_name
    Area_name = val.Area_name
    city = val.city
    full_add = val.full_add
    pincode = val.pincode
    user_type = val.user_type
    end_date = val.end_date
    book_name = val.book_name
    val_per = permanent_reg.objects.create(first_name = first_name, last_name = last_name, phone_number = phone_number,
     building_name = building_name, Area_name = Area_name, city = city, full_add = full_add, pincode = pincode, user_type = user_type,
     end_date = end_date, book_name = book_name )
    val_per.save()
    delete_val = temp_reg.objects.get(id = id)
    delete_val.delete()
    return redirect("/admin1")

def view(request, id):
    val = permanent_reg.objects.get(id=id)
    context = {
        'val':val
    }
    return render(request,'view.html', context)

def contact(request):
    val = contact_us.objects.all()
    context = {
        "val":val
    }
    return render(request, 'contect.html', context)

def notify_user(request):
    val = notify.objects.all()
    context = {
        "val":val
    }
    return render(request, 'notify.html', context)

def pray(request):
    val = prayer_request.objects.all()
    context = {
        "val":val
    }
    return render(request, "pray.html", context)
