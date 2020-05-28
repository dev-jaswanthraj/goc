from django.contrib import admin
from .models import home_details, book_details, contact_us, prayer_request, question

admin.site.register(book_details)
admin.site.register(home_details)
admin.site.register(contact_us)
admin.site.register(prayer_request)
admin.site.register(question)
