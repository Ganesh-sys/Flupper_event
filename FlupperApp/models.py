from django.db import models


# def nameFile(instance, filename):
#     return '/'.join(['images', str(instance.name), filename])


class Category(models.Model):
    name = models.CharField(max_length=64)


class Category_details(models.Model):
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=64)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    create_date = models.DateField(null=True, blank=True)
    event_image = models.ImageField(upload_to='Files/', default='nofile.pdf',null=True, blank=True)
#   images=models.ImageField('/images')
