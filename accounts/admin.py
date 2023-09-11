from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class MyUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'phone', 'is_staff', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email', 'first_name', 'last_name', 'phone'),
        }),
    )

    def __str__(self):
        return self.username

admin.site.register(MyUser, MyUserAdmin)

# admin.site.register(Customer)
# admin.site.register(CustomerAssessts)


from django.contrib import admin

from .models import Customer, CustomerAssessts

from django.contrib import admin
from django.utils.html import format_html

from .models import Customer, CustomerAssessts
from django.contrib import admin
from django.utils.html import format_html

from .models import Customer, CustomerAssessts
from django.contrib import admin
from django.utils.html import format_html

from .models import Customer, CustomerAssessts


from django.contrib import admin
from django.utils.html import format_html

from .models import Customer, CustomerAssessts


class CustomCustomerAssesstsInline(admin.TabularInline):
    model = CustomerAssessts
    extra = 1
    readonly_fields = ['display_image']
    fields = ['display_image', 'type_assesst']

    def display_image(self, obj):
        if obj.image_assesst:
            return format_html('<a href="{}" target="_blank"><img src="{}" width="100" height="100" /></a>',
                               obj.image_assesst.url, obj.image_assesst.url)
        return "-"
    display_image.short_description = 'Image'


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    inlines = [CustomCustomerAssesstsInline]
    list_display = ['full_name', 'identifyNo', 'place_Birth', 'place_identify_cut']
    search_fields = ['full_name', 'identifyNo']
    list_filter = ['place_Birth', 'place_identify_cut']
    readonly_fields=['stop_at']
from django.contrib import admin
from django.contrib.auth.models import Group
Group._meta.verbose_name_plural = "أقسام الموظفين"

#68D6E9
#2F6068
#1F62B7
#2471D3
# from django.contrib.auth.admin import GroupAdmin
# from django.contrib.auth.models import Group
# class CustomGroup(Group):
#     # Custom fields or modifications to existing fields

#     class Meta:
#         proxy = True
#         verbose_name = "Custom Group Name"
#         verbose_name_plural = "أقسام الموضفين"

# class CustomGroupAdmin(GroupAdmin):
#     # Customization for the admin interface
#     class Meta:
#         db_table = ''
#         managed = True
#         verbose_name = 'ModelName'
#         verbose_name_plural = 'ModelNames'

# admin.site.unregister(Group)
# admin.site.register(CustomGroup, CustomGroupAdmin)


# class CustomerAssesstsInline(admin.TabularInline):
#     model = CustomerAssessts
#     extra = 1


# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     inlines = [CustomerAssesstsInline]
#     list_display = ['full_name', 'identifyNo', 'place_Birth', 'place_identify_cut']
#     search_fields = ['full_name', 'identifyNo']
#     list_filter = ['place_Birth', 'place_identify_cut']


# @admin.register(CustomerAssessts)
# class CustomerAssesstsAdmin(admin.ModelAdmin):
#     list_display = ['customer', 'type_assesst', 'display_image']

#     def display_image(self, obj):
#         return format_html('<img src="{}" width="50" height="50" />', obj.image_assesst.url)
#     display_image.short_description = 'Image'

# class CustomerAssesstsInline(admin.TabularInline):
#     model = CustomerAssessts
#     extra = 1

#     def image_assesst_preview(self, obj):
#         if obj.image_assesst:
#             return format_html('<img src="{}" width="50" height="50" />', obj.image_assesst.url)
#         return "-"

#     image_assesst_preview.short_description = "Image Preview"


# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     inlines = [CustomerAssesstsInline]
#     list_display = ['full_name', 'identifyNo', 'place_Birth', 'place_identify_cut']
#     search_fields = ['full_name', 'identifyNo']
#     list_filter = ['place_Birth', 'place_identify_cut']


# admin.site.register(CustomerAssessts)
# class CustomerAssesstsInline(admin.TabularInline):
#     model = CustomerAssessts
#     extra = 1


# @admin.register(Customer)
# class CustomerAdmin(admin.ModelAdmin):
#     inlines = [CustomerAssesstsInline]
#     list_display = ['full_name', 'identifyNo', 'place_Birth', 'place_identify_cut']
#     search_fields = ['full_name', 'identifyNo']
#     list_filter = ['place_Birth', 'place_identify_cut']


# admin.site.register(CustomerAssessts)