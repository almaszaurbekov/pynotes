# Generated by Django 2.2.6 on 2019-10-24 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20191024_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='color',
        ),
        migrations.AddField(
            model_name='color',
            name='rgb',
            field=models.CharField(default='#532f8c', max_length=20, verbose_name='RGB'),
        ),
        migrations.AlterField(
            model_name='color',
            name='name',
            field=models.CharField(default='Стандартный', max_length=20, verbose_name='Название'),
        ),
    ]
