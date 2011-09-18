from django.contrib import admin
from addresses.models import Address


class AddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Address, AddressAdmin)

