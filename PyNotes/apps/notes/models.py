from django.db import models

# Create your models here.
class Color(models.Model):
    rgb = models.CharField('RGB', max_length=20, default="#532f8c")
    name = models.CharField('Название', max_length=20, default="Стандартный")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

class Category(models.Model):
    name = models.CharField('Название', max_length=30, default=None)
    color = models.ForeignKey(Color, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Note(models.Model):
    title = models.CharField('Титул', max_length=30, default=None)
    text = models.TextField('Заметка', default=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'