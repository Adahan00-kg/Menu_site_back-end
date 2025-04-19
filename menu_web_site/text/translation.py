from modeltranslation.translator import register, TranslationOptions
from .models import MainTitle, MiddleTitleText, MiddleSecondText, MenuTitle, AboutOur


@register(MainTitle)
class MainTitleTranslationOptions(TranslationOptions):
    fields = ('name_restaurant', 'kitchen', 'description', 'contact_info', 'location_text','location')


@register(MiddleTitleText)
class MiddleTitleTextTranslationOptions(TranslationOptions):
    fields = ('main_text', 'description', 'small_text')


@register(MiddleSecondText)
class MiddleSecondTextTranslationOptions(TranslationOptions):
    fields = ('main_text', 'description', 'small_text')


@register(MenuTitle)
class MenuTitleTranslationOptions(TranslationOptions):
    fields = ('small_text', 'text')


@register(AboutOur)
class AboutOurTranslationOptions(TranslationOptions):
    fields = ('address_text', 'address', 'time_text', 'time_open', 'time_close')

