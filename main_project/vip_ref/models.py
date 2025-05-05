from django.db import models
from django.conf import settings

# Create your models here.

def get_default():
    return str(settings.MEDIA_ROOT) + '/reply/BLANK.pdf'

class HOD(models.Model):
    hod= models.CharField(max_length=20)

    def __str__(self):
        return self.hod

class VIP(models.Model):
    vip= models.CharField(max_length=20)

    def __str__(self):
        return self.vip

class Reference(models.Model):
    
    pending_choices=[
        ('Pending','Pending'),
        ('Partial','Partial'),
        ('Replied','Replied')
    ]


    reference_dt = models.DateField()
    reference_subject = models.CharField(max_length=200)
    vip = models.ForeignKey(VIP, on_delete=models.CASCADE)
    vip_sub = models.CharField(max_length=60)
    reference_contents = models.TextField(null=True, blank=True)
    inward_dt = models.DateField()

    hod = models.ManyToManyField(HOD, blank=True, related_name='references')
    hod_reply = models.ManyToManyField(HOD, blank=True, related_name='references_reply')
    outward_ref = models.CharField(max_length=60, null=True, blank=True)
    outward_dt = models.DateField(null=True,blank=True)

    subject_file = models.FileField(upload_to='subject',null=True, blank=True, default=get_default)
    reply_file = models.FileField(upload_to='reply',null=True, blank=True, default=get_default)
    pending = models.CharField(choices= pending_choices,null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-inward_dt']

    def __str__(self):
        return f"{self.vip} subject: {self.reference_subject} date:{self.reference_dt}"