from django.contrib import admin

# Register your models here.
from .models import Association
from .models import Adherent

admin.site.register(Adherent)

class AssociationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Association, AssociationAdmin)
