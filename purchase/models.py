from django.db import models
from customer.models import Customer

# Create your models here.


class Purchase(models.Model):
    amount=models.FloatField(help_text='in India Rupees')
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='purchases')
