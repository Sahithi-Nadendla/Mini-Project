from django.contrib import admin
from .models import BooksLocations,BooksDetails
# Register your models here.
admin.site.register(BooksLocations)
admin.site.register(BooksDetails)