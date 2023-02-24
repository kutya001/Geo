from django.contrib import admin

from .models import (Farmer, Culture, Season, Place)


admin.site.register(Farmer)
admin.site.register(Culture)
admin.site.register(Season)
admin.site.register(Place)

# Register your models here.
