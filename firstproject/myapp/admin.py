from django.contrib import admin
from myapp.models import Employee, WorkHours, Salary, Login

# Register your models here.
admin.site.register(Employee)
admin.site.register(WorkHours)
admin.site.register(Salary)
admin.site.register(Login)