from django.db import models

# Create your models here.


class Book(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()


    def __str__(self) -> str:
        return self.name



class CustomManager(models.Manager):
    pass  

class FilterSortManager(models.Manager):

    def filter_methods(self):
        return self.filter(store_name__icontains='sto')


    def sort_methods(self,value,order):
        if order == "desc":
            value='-'+value
    
        return self.order_by(value)



class Store(models.Model):
    store_name = models.CharField(max_length=100)
    book = models.ManyToManyField(Book,related_name='book_store')   
    objects=CustomManager()
    another_objects=FilterSortManager()

    def __str__(self) -> str:
        return self.store_name 
