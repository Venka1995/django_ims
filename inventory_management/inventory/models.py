from django.db import models

# Create your models here.
class Device(models.Model):
    type=models.CharField(max_length=100,blank=False)
    price=models.IntegerField()
    choices = (
    ('Available','Item ready to perchased'),
    ('Sold','Currntly out of stock'),
    ('Restock','Item restock in few days'),
    )
    status=models.CharField(max_length=150,choices = choices,default='Sold')
    issues=models.CharField(max_length=150,default='No issues')

    class Meta:
        abstract = True


    def __str__(self):
        return 'Type: {0} price: {1}'.format(self.type, self.price)

class Laptop(Device):
    pass

class Mobile(Device):
    pass

class Desktop(Device):
    pass
