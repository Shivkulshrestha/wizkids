# Generated by Django 3.1.1 on 2020-09-12 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='image1',
            field=models.ImageField(default='', upload_to='school/static/school/images'),
        ),
    ]
