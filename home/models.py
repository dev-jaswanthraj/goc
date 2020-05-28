from django.db import models

class home_details(models.Model):
    main_image = models.FileField(null = True, blank = True)
    Promise_Of_the_Month = models.CharField(max_length = 10000)
    Promise_Of_the_Month_Proverb = models.CharField(max_length = 100)
    Promise_Of_the_day = models.CharField(max_length = 10000)
    Promise_Of_the_day_Proverb = models.CharField(max_length = 100)
    TODAY_WORD = models.TextField(max_length = 200)
    DAILY_THOUGHT = models.TextField(max_length = 100000)

class book_details(models.Model):
    book_name = models.CharField(max_length = 200)
    book_price = models.CharField(max_length = 4)
    book_dis_price = models.CharField(max_length = 4, null = True, blank = True)
    book_image = models.FileField(null = True, blank = True)
    book_perview_page_one = models.TextField(max_length=100000)
    book_preview_page_two = models.TextField(max_length=100000)

    def __str__(self):
        return self.book_name
    
class contact_us(models.Model):
    name = models.CharField(max_length = 200)
    mail = models.EmailField(max_length = 100)
    number = models.CharField(max_length = 10)
    message = models.TextField(max_length = 10000)

    def __str__(self):
        return self.name


class prayer_request(models.Model):
    name = models.CharField(max_length = 200)
    option = models.CharField(max_length = 500)
    number = models.CharField(max_length = 10)
    request = models.TextField(max_length = 10000)
    email = models.EmailField(max_length = 1000)

    def __str__(self):
        return self.name

# For the multi-Choice Question

class question(models.Model):
    ques = models.CharField(max_length = 500)
    pot1 = models.CharField(max_length = 100)
    pot2 = models.CharField(max_length = 100)
    pot3 = models.CharField(max_length = 100)
    pot4 = models.CharField(max_length = 100)
    crt_ans = models.CharField(max_length = 100)
    token = models.BooleanField(default=False)

    def __str__(self):
        return self.ques

    
