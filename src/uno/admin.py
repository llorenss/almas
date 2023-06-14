from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Person , Address

@admin.register(Person)
class PersonAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "age",
    )
    list_display_links = ("id",)
    list_editable = (
        "name",
        "age",
    )

@admin.register(Address)
class AddressAdmin(ModelAdmin):
    list_display = (
        "id",
        "street",
        "city",
        "person",
    )
    list_display_links = ("id",)
    list_editable = (
        "street",
        "city",
        "person",
    )