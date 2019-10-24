from django.db import models

# Create your models here.
class User(models.Model):
    login = models.CharField('Логин', max_length=10)
    password = models.CharField('Пароль', max_length=20)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Заметка', max_length=255)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'