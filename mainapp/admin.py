from django.contrib import admin
from .models import CustomerList, Table2

# To connect with DB
# py manage.py inspectdb > mainapp/models.py


# Register your models here.

class Table2Admin(admin.ModelAdmin):
    search_fields = ['name']

class Table1Admin(admin.ModelAdmin):
    list_display = ('custom_id', 'custom_name', 'reserve_date', 
    'rent_date', 'rent_time','return_date', 'return_time')


admin.site.register(Table2, Table2Admin)

admin.site.register(CustomerList, Table1Admin)