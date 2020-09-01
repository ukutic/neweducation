from django.db import models
#from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
    )
    mondai = models.TextField(blank=True)
    seikai = models.TextField(blank=True)
    kaisetu = models.TextField(blank=True)
 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)





# Create your models here.
