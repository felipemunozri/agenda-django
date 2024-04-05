from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'last_name', 'mobile', 'email',)
    search_fields = ('name', 'last_name', 'mobile', 'company',)
    list_filter = ('creation_date',)

# Register your models here.
admin.site.register(Contact, ContactAdmin)