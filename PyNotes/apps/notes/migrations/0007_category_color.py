# Generated by Django 2.2.6 on 2019-10-24 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_auto_20191024_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='color',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='notes.Color'),
        ),
    ]