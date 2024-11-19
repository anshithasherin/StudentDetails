from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    admission_no=models.IntegerField(unique=True)
    course=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    photo=models.ImageField(upload_to='student_image')