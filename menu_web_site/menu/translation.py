from .models import Category, MenuItem, Extras
from modeltranslation.translator import TranslationOptions, register


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(MenuItem)
class MenuItemTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(Extras)
class ExtrasTranslationOptions(TranslationOptions):
    fields = ('extra_name',)
