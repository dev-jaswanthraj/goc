from django.shortcuts import render , redirect
from .models import home_details, book_details, contact_us, prayer_request, question
from admin1.models import temp_reg, notify
from django.http import HttpResponse

def home(request):
    val  = home_details.objects.get(id = 1)
    para = val.DAILY_THOUGHT[0:100]
    print(para)
    context = {
        "val":val,
        "para":para
    }
    return render(request, "base.html", context)

def book(request):
    val = book_details.objects.all()
    if len(val) == 0:
        message = "No Book is found !!!"
        context = {
            "message":message
        }  
    context = {
        "val":val,
    }

    return render(request, "page.html", context)

def contact_us_fun(request):
    return render(request, "contactus.html")

def save(request):
    if request.method == 'POST':
        val1 = request.POST['name']
        val2 = request.POST['mail']
        val3 = request.POST['number']
        val4 = request.POST['mess']
        val = contact_us.objects.create(name = val1, mail = val2, number = val3, message = val4)
        val.save()    
    return redirect("/contactus")

def describe(request, id):
    val = book_details.objects.get(id = id)
    context = {
        "val":val
    }
    return render(request, "describe.html", context)

def reg_one(request, id):
    book = book_details.objects.get(id = id)
    context = {
       "book":book 
    }
    return render(request, 'buynow.html', context)

def save_in_db_one(request):

    if request.method == "POST":
        first_name = request.POST['first_name'] 
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        building_name = request.POST['building_name']
        Area_name = request.POST['Area_name']
        city = request.POST['city']
        full_add = request.POST['full_add']
        pincode = request.POST['pincode']
        user_type ="BUYER"
        book_name = request.POST['book_name']
        val_per = temp_reg.objects.create(first_name = first_name, last_name = last_name, phone_number = phone_number,
        building_name = building_name, Area_name = Area_name, city = city, full_add = full_add, pincode = pincode, user_type = user_type,
         book_name = book_name )
        val_per.save() 
   
        return redirect("/book")   


def event(request):
    return render(request, 'event.html')

def notify_up(request):
    if request.method == 'POST':
        val1 = request.POST['email']
        val2 = request.POST['psw']

        val = notify.objects.create(name = val1 , number = val2)
        val.save()
    return redirect("/event")

def prayer(request):
    return render(request, "prayerrequest.html")

def prayer_save(request):
    if request.method == "POST":
        val1 = request.POST['name']
        val2 = request.POST['number']
        val3 = request.POST['request']
        val4 = request.POST['address']
        val5 = request.POST['email']
        val = prayer_request.objects.create(name = val1, number = val2, request = val3, option = val4, email = val5)
        val.save()
        context = {
            "val":"Your request is saved!"
        }
        return render(request, "prayerrequest.html", context)

def testimony(request):
    return render(request, 'testimony.html')

def galary(request):
    return render(request, 'gallary.html')
        
def kids(request):
    return render(request, 'kids.html')

def start_quiz(request):
    return render(request, 'quiz.html')