from django.contrib import admin
from .models import CodigoMorse, WordsTable


class CodigoMorseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'character',
        'code',
    )

    #
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    # #

    search_fields = (
        'character',
    )


admin.site.register(CodigoMorse, CodigoMorseAdmin)
admin.site.register(WordsTable)
