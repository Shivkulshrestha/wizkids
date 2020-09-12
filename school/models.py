from django.db import models


# Create your models here.

# these are our model for photos which are shown in gallery page


class Photos(models.Model):
    block_name = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=100, default="")
    image1 = models.ImageField(upload_to='school/images/', default="")
    image2 = models.ImageField(upload_to='school/images/', default="")
    image3 = models.ImageField(upload_to='school/images/', default="")
    image4 = models.ImageField(upload_to='school/images/', default="")
    image5 = models.ImageField(upload_to='school/images/', default="")
    image6 = models.ImageField(upload_to='school/images/', default="")
    image7 = models.ImageField(upload_to='school/images/', default="")
    image8 = models.ImageField(upload_to='school/images/', default="")
    image9 = models.ImageField(upload_to='school/images/', default="")
    image10 = models.ImageField(upload_to='school/images/', default="")

    def __str__(self):  # this function works to show the name of particular variable on the admin panel
        return self.block_name  # in this case the variable is block_name


# this class is created to collect the imformation from the user input in contact form
class Soochna(models.Model):
    name = models.CharField(max_length=50, blank="")
    email = models.CharField(max_length=50, blank="")
    phone = models.CharField(max_length=10, blank="")
    desc = models.CharField(max_length=3000, blank="")

    def __str__(self):
        return self.name


# this class is created to collect the imformation from the user input in admission form
class Admission(models.Model):
    student_name = models.CharField(max_length=50, blank="")
    admission_class = models.CharField(max_length=50, blank="")
    parents_name = models.CharField(max_length=50, blank="")
    phone_no = models.CharField(max_length=10, blank="")
    email = models.CharField(max_length=50, blank="")
    address = models.CharField(max_length=300, blank="")

    def __str__(self):
        return self.student_name


class Download(models.Model):
    file_name = models.CharField(max_length=200, blank="")
    file = models.FileField(upload_to='app_1/docs', default="")
    desc = models.CharField(max_length=1000, blank="")
    new = models.BooleanField(default="False")
    pub_date = models.DateField(default='django.utils.timezone.now()')

    def __str__(self):
        return self.file_name


class Donations(models.Model):
    name = models.CharField(max_length=200, blank="")
    email = models.CharField(max_length=200, blank="")
    phone = models.CharField(max_length=200, blank="")
    desc = models.CharField(max_length=5000, blank="")

    def __str__(self):
        return self.name
