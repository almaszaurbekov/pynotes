from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Название', max_length=30, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Note(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    title = models.CharField('Титул', max_length=30, default=None)
    text = models.TextField('Заметка', default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'