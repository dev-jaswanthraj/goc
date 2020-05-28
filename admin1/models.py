from django.db import models

class temp_reg(models.Model):
    CHOICE =(
        ('DONATION','DONATION'),
        ('SUBSCRIBER', 'SUBSCRIBER'),
        ('BUYER', 'BUYER')
    )
    first_name = models.CharField(max_length = 100, blank = False)
    last_name = models.CharField(max_length = 100, blank = True, null = True)
    phone_number = models.CharField(max_length = 10, blank = False)
    building_name = models.CharField(max_length = 100, blank = False)
    Area_name = models.CharField(max_length = 100, blank = False)
    city = models.CharField(max_length = 100, blank = False)
    full_add = models.TextField(max_length = 500, blank = False)
    pincode = models.CharField(max_length = 6, blank = False)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(blank = True, null = True)
    user_type = models.CharField(max_length = 40, choices = CHOICE, blank = True)
    book_name = models.CharField(max_length = 40, blank = True, null = True)

    def __str__(self):
        return self.first_name 
    
class permanent_reg(models.Model):
    CHOICE =(
        ('DONATION','DONATION'),
        ('SUBSCRIBER', 'SUBSCRIBER'),
        ('BUYER', 'BUYER')
    )
    first_name = models.CharField(max_length = 100, blank = False)
    last_name = models.CharField(max_length = 100, blank = True, null = True)
    phone_number = models.CharField(max_length = 10, blank = False)
    building_name = models.CharField(max_length = 100, blank = False)
    Area_name = models.CharField(max_length = 100, blank = False)
    city = models.CharField(max_length = 100, blank = False)
    full_add = models.TextField(max_length = 500, blank = False)
    pincode = models.CharField(max_length = 6, blank = False)
    user_type = models.CharField(max_length = 40, choices = CHOICE, blank = False, null = True)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateField(blank = True, null = True)
    book_name = models.CharField(max_length = 40, blank = True, null = True)

    def __str__(self):
        return self.first_name 

class notify(models.Model):
    name = models.CharField(max_length = 100)
    number = models.CharField(max_length = 10)

    def __str__(self):
        return self.name