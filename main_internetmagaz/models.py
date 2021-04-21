from django.db import models
from uuid import uuid4
from os import path

# Create your models here.

class Category(models.Model): # Category of pruducts(man, woman,sport, i.t.d)
    def get_file_name(self, filename):
        exc = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{exc}'
        return path.join('media/images/categories', filename)



    title = models.CharField(max_length=16, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    category_order = models.IntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}:{self.category_order}'

class Kind(models.Model): # kind of products in category(костюмы, платья, и.т.д.)

    def get_file_name(self, filename):
        exc = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{exc}'
        return path.join('media/images/kinds', filename)

    title = models.CharField(max_length=30, unique=True)
    photo = models.ImageField(upload_to=get_file_name)
    kind_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    des = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.price}'

class Info(models.Model):
    title = models.CharField(max_length=30, unique=True)
    maz_infp = models.CharField(max_length=300)
    photo = models.ImageField()
    is_visible = models.BooleanField(default=True)
    des = models.CharField(max_length=400,unique=True)

    def __str__(self):
        return f'{self.title}'

class Phone(models.Model):
    phone = models.CharField(max_length=14, unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.phone}'

class Adress(models.Model):
    city = models.CharField(max_length=20)
    street = models.CharField(max_length=30)
    building = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.city}, {self.street}, {self.building}'

class OpenningHours(models.Model):
    day = models.CharField(max_length=10)
    hours = models.CharField(max_length=12)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.day}: {self.hours}'

class MagInfo(models.Model):
    adress_id = models.ForeignKey(Adress, on_delete=models.CASCADE)
    phone_id = models.ForeignKey(Phone, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.adress_id}, {self.phone_id}'

class Message(models.Model):
    user_name = models.CharField(max_length=40)
    user_email = models.EmailField()
    user_message = models.CharField(max_length=400)
    pub_date = models.DateField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user_name}, {self.user_email}, {self.user_message[:20]}'


class MensCostume(models.Model): # pruduct in kind of prodcts ( костюм, платье, и.т.д.)

    def get_file_name(self, filename):
        exc = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{exc}'
        return path.join('media/images/menscostume', filename)

    title = models.CharField(max_length=30, unique=True)
    photo = models.ImageField(upload_to=get_file_name,default=True)
    kind_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    des = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Kind, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title}, {self.price}'


#  Это Пока не использую

class MensBlouse(models.Model):

    def get_file_name(self, filename):
        exc = filename.strip().split('.')[-1]
        filename = f'{uuid4()}.{exc}'
        return path.join('media/images/mensblouse', filename)

    title = models.CharField(max_length=30, unique=True)
    photo = models.ImageField(upload_to=get_file_name, default=True)
    kind_order = models.IntegerField()
    is_visible = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    des = models.CharField(max_length=150, unique=True)
    category = models.ForeignKey(Kind, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title}, {self.price}'