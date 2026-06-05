from django.db import models
from cloudinary.models import CloudinaryField

class Phone(models.Model):
    CATEGORY={
        'Apple':'Apple',
        'Samsung':'Samsung',
        'Google':'Google',
        'Xiaomi':'Xiaomi',
        'OnePlus':'OnePlus',
        'Hoco':'Hoco',
    }
    category=models.CharField(choices=CATEGORY)
    name=models.CharField()
    price=models.IntegerField()
    icon_class=models.CharField(blank=True,null=True,default='nothing')
    brand=models.CharField(choices=CATEGORY)
    short=models.CharField()
    camera=models.CharField()
    old_price=models.IntegerField(null=True,blank=True)
    icon = CloudinaryField('images',null=True)








