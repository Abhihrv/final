from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'user_type')

class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

class GenderAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

class AddressTypeAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'apt', 'city', 'pincode', 'country', 'address_type', 'state')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', 'gender', 'address_home', 'address_current', 'designation')

class DesginationAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

class TeachingAdmin(admin.ModelAdmin):
    list_display = ('user', 'designation', 'age', 'gender', 'address')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('user', 'designation', 'age', 'gender', 'address')

admin.site.register(User, UserAdmin)
admin.site.register(UserType, UserTypeAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(AddressType, AddressTypeAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Desgination, DesginationAdmin)
admin.site.register(Teaching, TeachingAdmin)
admin.site.register(Staff, StaffAdmin)