from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')
    category_connect = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return self.title



class Extras(models.Model):
    item_connect = models.ManyToManyField(MenuItem,related_name='extra', null=True,blank=True)
    extra_price = models.DecimalField(max_digits=6, decimal_places=2,blank=True)
    extra_name = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f'{self.extra_name}'