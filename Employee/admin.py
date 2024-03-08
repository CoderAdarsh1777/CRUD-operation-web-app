from django.contrib import admin
from Employee.models import Employees

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'phone')

admin.site.register(Employees,EmployeeAdmin)
# Register your models here.
