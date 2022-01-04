from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Student

# Register your models here.
@admin.register(Student)
class StudentAdmmin(admin.ModelAdmin):
    list_display =('id','name','email','password')   