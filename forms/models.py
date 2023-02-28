from django.db import models
# Create your models here.

class Details(models.Model):
    first_name = models.CharField(max_length=100,null=False,blank=False)
    last_name = models.CharField(max_length=100,null=False,blank=False)
    email = models.EmailField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name