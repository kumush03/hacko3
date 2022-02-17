from django.db import models

# Create your models here.
class Contact_us(models.Model):
    email = models.CharField(max_length=50, verbose_name='Почта')
    sent_at = models.DateTimeField(auto_now_add=True,verbose_name='Отправлено')


class Category(models.Model):
    title =models.CharField(max_length=50,verbose_name=' Категория')
    images = models.ImageField(upload_to='core',verbose_name='Изображение')

    def __str__(self):
        return self.title


class Foodcard(models.Model):
    name= models.CharField(max_length=50,verbose_name='Название еды')
    price =models.IntegerField(verbose_name='Цена')
    image=models.ImageField(upload_to='core', verbose_name='Изоброжение')
    category= models.ForeignKey(Category, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

        