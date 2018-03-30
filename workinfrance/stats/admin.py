from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from workinfrance.stats.models import DossierAPT


class DossierAPTAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'ds_id',
        'status',
        'created',
        'department',
        'apt_start_date',
        'apt_end_date',
        'accompagnateurs',
    )
    search_fields = ['ds_id']
    list_per_page = 100
    list_filter = ['status', 'department']
    ordering = ('-created_at',)
    list_display_links = ['id', 'ds_id']
    date_hierarchy = 'created_at'

    def created(self, obj):
        return obj.created_at.strftime("%d/%m/%Y %H:%M")
    created.short_description = _("Créé le")

    def apt_start_date(self, obj):
        try:
            return obj.apt_start_date.strftime("%d/%m/%Y")
        except AttributeError:
            return obj.apt_start_date
    apt_start_date.short_description = _("Début APT")

    def apt_end_date(self, obj):
        try:
            return obj.apt_end_date.strftime("%d/%m/%Y")
        except AttributeError:
            return obj.apt_end_date
    apt_end_date.short_description = _("Fin APT")


admin.site.register(DossierAPT, DossierAPTAdmin)
