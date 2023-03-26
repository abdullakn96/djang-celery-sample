from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Store
from django.db.models import Prefetch

# Create your views here.



def prefetch_related_view(request):

    #Backward many to many
    # books=Book.objects.all().prefetch_related('book_store')
    # print(books)
    # # for book in books:
    # #     print(book.name,book.book_store.all())



    #forward many to many
    # print("forward manay to many")
    # stores=Store.objects.all().prefetch_related('book')    
    # print(stores) 
    # for store in stores:
    #     print(store.store_name,store.book.all())



    #perform better with filter()

    stores=Store.objects.all().prefetch_related(Prefetch('book',queryset=Book.objects.filter(price__range=(100,200))))

    for store in stores:
        print(store.store_name,store.book.all())

        

    # print("normal way -------------")
    # normal_way=Store.objects.all()   
    # print(normal_way) 
    # for store in normal_way:
    #     print(store.book.all())      
    # return HttpResponse()




def manager_functions(request):
    obj=Store.objects.all()
    print(obj)

    obj1=Store.another_objects.filter_methods()
    print(obj1)
    print("---------------------")


    sort_result = Store.another_objects.sort_methods('store_name','asc')
    print(sort_result)

    return HttpResponse(True)