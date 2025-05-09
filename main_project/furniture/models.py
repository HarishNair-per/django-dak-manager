from django.db import models
from django_advance_thumbnail import AdvanceThumbnailField

# Create your models here.

class AssetDesc(models.Model):
    asset_name= models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.asset_name

        

class Furniture(models.Model):
    
    room_choices=[
        ('2310','HR Director Room'),
        ('2311','HR TS Room'),
        ('2313','HR Staff Room'),
        ('231V','HR Visting Room'),
        ('2308','HR Conference Room'),
        ('231R','HR Rest Room'),
    ]

    furniture_choices=[
        ('1','Chair Normal'),
        ('2','Table'),
        ('3','Almirah'),
        ('4','Bookself'),
        ('5','PC'),
        ('6','Printer'),
        ('7','Color Printer'),
        ('8','Chair Executive'),
    ]

    furniture_type= models.ForeignKey(AssetDesc, on_delete=models.CASCADE)
    furniture_qty= models.PositiveSmallIntegerField(null=True, blank=True)
    furniture_dt_receipt= models.DateField(null=True, blank=True)
    furniture_make= models.CharField(max_length=60)
    furniture_model= models.CharField(max_length=60,null=True, blank=True)
    furniture_serial= models.CharField(max_length=60,null=True, blank=True)
    furniture_room= models.CharField(choices= room_choices)
    furniture_image= models.ImageField(upload_to='assets',null=True, blank=True)
    thumbnail = AdvanceThumbnailField(source_field='furniture_image', upload_to='thumbnails/', null=True, blank=True,
                                      size=(300, 300)) 

    
    furniture_remarks= models.TextField(null=True, blank=True)
    furniture_updated = models.DateTimeField(auto_now=True)
    furniture_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-furniture_dt_receipt']

    def __str__(self):
        return f"{self.furniture_type} - {self.furniture_make}"