from django.contrib import admin
from .models import MenuItem, Category, Extras
from modeltranslation.admin import TranslationAdmin


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ("category_name", )

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(MenuItem)
class MenuItemAdmin(TranslationAdmin):
    list_display = ("title", "description", "price", "image", "category_connect")

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Extras)
class ExtrasAdmin(TranslationAdmin):
    list_display = ("get_item_connect", "extra_price", "extra_name")

    def get_item_connect(self, obj):
        return ", ".join([str(item) for item in obj.item_connect.all()])
    get_item_connect.short_description = "Items"

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
