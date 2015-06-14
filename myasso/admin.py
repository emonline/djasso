from django.contrib import admin

# Register your models here.
from .models import Association
from .models import Adherent

admin.site.register(Adherent)

class AdherentInLine(admin.TabularInline):
    model = Adherent

class AssociationAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    inlines = [
        AdherentInLine,
    ]

admin.site.register(Association, AssociationAdmin)
