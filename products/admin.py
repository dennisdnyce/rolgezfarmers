from django.contrib import admin
from .models import Farm_produces
from .models import Latest_farm_produces
from .models import Rolgezfarm_services
from .models import Rolgezfarm_contacts
# Register your models here.

admin.site.register(Farm_produces)
admin.site.register(Latest_farm_produces)
admin.site.register(Rolgezfarm_services)
admin.site.register(Rolgezfarm_contacts)
