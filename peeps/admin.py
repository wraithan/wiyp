from django.contrib import admin
from peeps.models import Peep


class PeepAdmin(admin.ModelAdmin):
    pass


admin.site.register(Peep, PeepAdmin)

