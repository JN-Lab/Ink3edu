from django.db import models

class Training(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Section(models.Model):
    pass

class Chapter(models.Model):
    pass

class Status(models.Model):
    pass

class Category(models.Model):
    pass