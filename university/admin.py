from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'user_type')

class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'apt', 'city', 'pincode', 'country', 'state')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user','address')

class TeachingAdmin(admin.ModelAdmin):
    list_display = ('user', 'address')

class UniversityAdminAdmin(admin.ModelAdmin):
    list_display = ('user', 'address')

admin.site.register(User, UserAdmin)
admin.site.register(UserType, UserTypeAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teaching, TeachingAdmin)
admin.site.register(UniversityAdmin, UniversityAdminAdmin)