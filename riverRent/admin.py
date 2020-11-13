from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *


# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Trip_Detail)
admin.site.register(Water_Craft)
admin.site.register(Trip_Package)
admin.site.register(Invoice)
admin.site.register(Invoice_Line)
