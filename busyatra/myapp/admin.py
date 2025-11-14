from django.contrib import admin
from django.contrib.auth.models import User

from myapp.models import admintbl, routestbl, managebustbl, managequotastbl, booknowtbl

# Register your models here.
admin.site.register(admintbl)
admin.site.register(routestbl)
admin.site.register(managebustbl)
admin.site.register(managequotastbl)
admin.site.register(booknowtbl)

