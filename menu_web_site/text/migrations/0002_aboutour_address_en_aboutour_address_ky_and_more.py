# Generated by Django 5.2 on 2025-04-18 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutour',
            name='address_en',
            field=models.CharField(max_length=500, null=True, verbose_name='местоположения адресса'),
        ),
        migrations.AddField(
            model_name='aboutour',
            name='address_ky',
            field=models.CharField(max_length=500, null=True, verbose_name='местоположения адресса'),
        ),
        migrations.AddField(
            model_name='aboutour',
            name='address_ru',
            field=models.CharField(max_length=500, null=True, verbose_name='местоположения адресса'),
        ),
        migrations.AddField(
            model_name='aboutour',
            name='address_text_en',
            field=models.CharField(max_length=150, null=True, verbose_name='адрес'),
        ),
        migrations.AddField(
            model_name='aboutour',
            name='address_text_ky',
            field=models.CharField(max_length=150, null=True, verbose_name='адрес'),
        ),
        migrations.AddField(
            model_name='aboutour',
            name='address_text_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='адрес'),
        ),
        migrations.AddField(
            model_name='aboutour',
            name='time_close_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutour',
            name='time_close_ky',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutour',
            name='time_close_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutour',
            name='time_open_en',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutour',
            name='time_open_ky',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutour',
            name='time_open_ru',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutour',
            name='time_text_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='aboutour',
            name='time_text_ky',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='aboutour',
            name='time_text_ru',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='maintitle',
            name='contact_info_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='maintitle',
            name='contact_info_ky',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='maintitle',
            name='contact_info_ru',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='maintitle',
            name='description_en',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='описания'),
        ),
        migrations.AddField(
            model_name='maintitle',
            name='description_ky',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='описания'),
        ),
        migrations.AddField(
            model_name='maintitle',
            name='description_ru',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='описания'),
        ),
        migrations.AddField(
            model_name='maintitle',
            name='kitchen_en',
            field=models.CharField(max_length=100, null=True, verbose_name='кухня'),
        ),
        migrations.AddField(
            model_name='maintitle',
            name='kitchen_ky',
            field=models.CharField(max_length=100, null=True, verbose_name='кухня'),
        ),
        migrations.AddField(
            model_name='maintitle',
            name='kitchen_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='кухня'),
        ),
        migrations.AddField(
            model_name='maintitle',
            name='location_text_en',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='maintitle',
            name='location_text_ky',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='maintitle',
            name='location_text_ru',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='maintitle',
            name='name_restaurant_en',
            field=models.CharField(max_length=100, null=True, verbose_name='названия ресторана'),
        ),
        migrations.AddField(
            model_name='maintitle',
            name='name_restaurant_ky',
            field=models.CharField(max_length=100, null=True, verbose_name='названия ресторана'),
        ),
        migrations.AddField(
            model_name='maintitle',
            name='name_restaurant_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='названия ресторана'),
        ),
        migrations.AddField(
            model_name='menutitle',
            name='small_text_en',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='menutitle',
            name='small_text_ky',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='menutitle',
            name='small_text_ru',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='menutitle',
            name='text_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='menutitle',
            name='text_ky',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='menutitle',
            name='text_ru',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='middlesecondtext',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='middlesecondtext',
            name='description_ky',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='middlesecondtext',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='middlesecondtext',
            name='main_text_en',
            field=models.CharField(max_length=150, null=True, verbose_name='главный текст в середине '),
        ),
        migrations.AddField(
            model_name='middlesecondtext',
            name='main_text_ky',
            field=models.CharField(max_length=150, null=True, verbose_name='главный текст в середине '),
        ),
        migrations.AddField(
            model_name='middlesecondtext',
            name='main_text_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='главный текст в середине '),
        ),
        migrations.AddField(
            model_name='middlesecondtext',
            name='small_text_en',
            field=models.CharField(max_length=25, null=True, verbose_name='маленький тест сверху'),
        ),
        migrations.AddField(
            model_name='middlesecondtext',
            name='small_text_ky',
            field=models.CharField(max_length=25, null=True, verbose_name='маленький тест сверху'),
        ),
        migrations.AddField(
            model_name='middlesecondtext',
            name='small_text_ru',
            field=models.CharField(max_length=25, null=True, verbose_name='маленький тест сверху'),
        ),
        migrations.AddField(
            model_name='middletitletext',
            name='description_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='middletitletext',
            name='description_ky',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='middletitletext',
            name='description_ru',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='middletitletext',
            name='main_text_en',
            field=models.CharField(max_length=150, null=True, verbose_name='главный текст в середине '),
        ),
        migrations.AddField(
            model_name='middletitletext',
            name='main_text_ky',
            field=models.CharField(max_length=150, null=True, verbose_name='главный текст в середине '),
        ),
        migrations.AddField(
            model_name='middletitletext',
            name='main_text_ru',
            field=models.CharField(max_length=150, null=True, verbose_name='главный текст в середине '),
        ),
        migrations.AddField(
            model_name='middletitletext',
            name='small_text_en',
            field=models.CharField(max_length=25, null=True, verbose_name='маленький тест сверху'),
        ),
        migrations.AddField(
            model_name='middletitletext',
            name='small_text_ky',
            field=models.CharField(max_length=25, null=True, verbose_name='маленький тест сверху'),
        ),
        migrations.AddField(
            model_name='middletitletext',
            name='small_text_ru',
            field=models.CharField(max_length=25, null=True, verbose_name='маленький тест сверху'),
        ),
    ]
