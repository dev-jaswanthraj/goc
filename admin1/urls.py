from django.urls import path
from . import views
from home import views as views1


urlpatterns = [
    path('', views.home, name = "home1"),
    path('add/<str:id>/', views.add, name = "add"),
    path('view/<str:id>', views.view, name = "view"),
    path('home/', views1.home, name = "home"),
    path('contect/', views.contact, name = "contact"),
    path('notify/', views.notify_user, name = "notify_up"),
    path('pray', views.pray, name = "pray")
]