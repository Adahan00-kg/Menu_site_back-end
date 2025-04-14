from django.db import models


class MainTitle(models.Model):
    name_restaurant = models.CharField(max_length=100,verbose_name='названия ресторана')
    kitchen = models.CharField(max_length=100,verbose_name='кухня')
    description =  models.CharField(max_length=250,null=True,blank=True,verbose_name='описания')
    contact_info = models.CharField(max_length=150)
    number = models.CharField(max_length=50)
    location_text = models.CharField(max_length=25)
    location = models.CharField(max_length=500)

class MiddleTitleText(models.Model):
    main_text = models.CharField(max_length=150,verbose_name='главный текст в середине ')
    description = models.TextField(null=True,blank=True)
    small_text = models.CharField(max_length=25,verbose_name='маленький тест сверху')



class MiddleSecondText(models.Model):
    main_text = models.CharField(max_length=150,verbose_name='главный текст в середине ')
    description = models.TextField(null=True,blank=True)
    small_text = models.CharField(max_length=25,verbose_name='маленький тест сверху')


class MenuTitle(models.Model):
    small_text = models.CharField(max_length=25)
    text = models.CharField(max_length=250)



class AboutOur(models.Model):
    address_text = models.CharField(max_length=150,verbose_name='адрес')
    address = models.CharField(max_length=500,verbose_name='местоположения адресса')
    time_text = models.CharField(max_length=150)
    time_open = models.CharField(max_length=200)
    time_close = models.CharField(max_length=200)
    address_photo = models.ImageField(upload_to='address',null=True,blank=True)
