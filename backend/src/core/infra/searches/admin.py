from django.contrib import admin

from core.infra.searches.models import Search


@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('search_id', 'finished')
