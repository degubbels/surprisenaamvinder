from django.contrib import admin
from solo.admin import SingletonModelAdmin

from naamvinder.models import Naam, Config

# Register your models here.
admin.site.register(Naam)

# Config singleton
admin.site.register(Config, SingletonModelAdmin)