from django.contrib import admin
from .models import *
# Register your models here.
class apartmentAdmin(admin.ModelAdmin):
    serviceTitle = ("roomSize","noOfWindows","isMetro")

class EmployeeAdmin(admin.ModelAdmin):
     serviceTitle = ("Name","EmpID","Domine")



admin.site.register(Appartments,apartmentAdmin)

admin.site.register(Employee,EmployeeAdmin)