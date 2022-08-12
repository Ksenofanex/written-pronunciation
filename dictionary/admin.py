from django.contrib import admin

from dictionary.models import Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = (
        "english",
        "turkish",
        "author",
        "is_approved",
        "date_created",
        "date_updated",
    )
    search_fields = ("english", "turkish", "author__username")
    list_select_related = ("author",)
    list_filter = ("date_created", "date_updated")
    list_editable = ("is_approved",)

    fieldsets = (
        (
            "Main",
            {
                "fields": (
                    "english",
                    "turkish",
                    "author",
                )
            },
        ),
        (
            "Approval",
            {"fields": ("is_approved",)},
        ),
    )
