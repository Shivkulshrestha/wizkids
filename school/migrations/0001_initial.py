# Generated by Django 3.1 on 2020-08-29 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(blank='', max_length=50)),
                ('admission_class', models.CharField(blank='', max_length=50)),
                ('parents_name', models.CharField(blank='', max_length=50)),
                ('phone_no', models.CharField(blank='', max_length=10)),
                ('email', models.CharField(blank='', max_length=50)),
                ('address', models.CharField(blank='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank='', max_length=200)),
                ('email', models.CharField(blank='', max_length=200)),
                ('phone', models.CharField(blank='', max_length=200)),
                ('desc', models.CharField(blank='', max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank='', max_length=200)),
                ('file', models.FileField(default='', upload_to='app_1/docs')),
                ('desc', models.CharField(blank='', max_length=1000)),
                ('new', models.BooleanField(default='False')),
                ('pub_date', models.DateField(default='django.utils.timezone.now()')),
            ],
        ),
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_name', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=100)),
                ('image1', models.ImageField(default='', upload_to='media/images/')),
                ('image2', models.ImageField(default='', upload_to='media/images/')),
                ('image3', models.ImageField(default='', upload_to='media/images/')),
                ('image4', models.ImageField(default='', upload_to='media/images/')),
                ('image5', models.ImageField(default='', upload_to='media/images/')),
                ('image6', models.ImageField(default='', upload_to='media/images/')),
                ('image7', models.ImageField(default='', upload_to='media/images/')),
                ('image8', models.ImageField(default='', upload_to='media/images/')),
                ('image9', models.ImageField(default='', upload_to='media/images/')),
                ('image10', models.ImageField(default='', upload_to='media/images/')),
            ],
        ),
        migrations.CreateModel(
            name='Soochna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank='', max_length=50)),
                ('email', models.CharField(blank='', max_length=50)),
                ('phone', models.CharField(blank='', max_length=10)),
                ('desc', models.CharField(blank='', max_length=3000)),
            ],
        ),
    ]
