from django.urls import path
from . import views
from admin1 import views as views1

urlpatterns = [
    path("", views.home, name = "home"),
    path('admin1/', views1.home, name = "admin1"),
    path('book/', views.book, name = "book"),
    path('contactus/', views.contact_us_fun, name = "contact_us"),
    path('save/', views.save, name = "save"),
    path('describe/<str:id>/', views.describe, name = "describe"),
    path("reg/<str:id>", views.reg_one, name = "reg_one"),
    path('save_in_db_one/', views.save_in_db_one, name = "save_in_db_one"),
    path('event/', views.event, name = "event"),
    path('notify/',views.notify_up, name = "notify"),
    path('prayer/', views.prayer, name = "prayer"),
    path("prayer_save/", views.prayer_save, name = "prayer_save"),
    path("testimony/", views.testimony, name = "testimony"),
    path('galary/', views.galary, name = "galary"),
    path('kids/', views.kids, name = "kids"),
    path('start_quiz/', views.start_quiz, name = "start_quiz"),
]