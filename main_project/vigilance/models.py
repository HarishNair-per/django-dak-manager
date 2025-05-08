from django.db import models
from vip_ref.models import HOD
from django.conf import settings

def get_default():
    return str(settings.MEDIA_ROOT) + '/BLANK.pdf'
# Create your models here.


class Complainant(models.Model):
    name = models.CharField(max_length=200)
    address= models.TextField(null=True, blank=True)
    mobile= models.DecimalField(max_digits=10, decimal_places=0, default=0, null=True)

    def __str__(self):
        return self.name

class Vigilance(models.Model):
    
    pending_choices=[
        ('Pending','Pending'),
        ('Partial','Partial'),
        ('Replied','Replied')
    ]

    vigilance_ref_no=models.CharField(max_length=100, null=True, blank=True)
    vigilance_dt= models.DateField(null=True,blank=True)
    vigilance_eoffice= models.PositiveIntegerField(null=True, blank=True)
    vigilance_subject= models.CharField(max_length=200)
    vigilance_complainant=models.ForeignKey(Complainant, on_delete= models.CASCADE)
    
    vigilance_contents= models.TextField(null=True, blank=True)
    vigilance_inward_dt= models.DateField(null=True,blank=True)

    vigilance_hod = models.ManyToManyField(HOD, blank=True, related_name='HOD')
    vigilance_hod_reply = models.ManyToManyField(HOD, blank=True, related_name='HOD_reply')
    vigilance_outward_ref= models.CharField(max_length=60, null=True, blank=True)
    vigilance_outward_dt= models.DateField(null=True,blank=True)

    vigilance_subject_file = models.FileField(upload_to='vig_subject',null=True, blank=True, default=get_default)
    vigilance_reply_file = models.FileField(upload_to='vig_reply',null=True, blank=True, default=get_default)
    vigilance_pending= models.CharField(choices= pending_choices,null=True, blank=True)
    vigilance_remarks= models.TextField(null=True, blank=True)
    vigilance_updated = models.DateTimeField(auto_now=True)
    vigilance_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-vigilance_inward_dt']

    def __str__(self):
        return f"{self.vigilance_dt} - complainant: {self.vigilance_complainant} - subject: {self.vigilance_subject}"