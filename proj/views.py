import re
from unittest import result
from django.http import HttpResponse, request
from blogpost.models import Blogs, Comments, Post
from bookapp.models import Book, Store
from customer.models import Customer
from purchase.models import Purchase
from django.db.models import Avg,Sum,Count


def home_view(request):
    #average customer age
    # result=Customer.objects.aggregate(Avg('age'))
    # if isinstance(result,dict):
    #     print("dict value")


    #Total customer age
    # result=Customer.objects.aggregate(Sum('age'))

    #Average age of customer older than 30
    result=Customer.objects.filter(age__gte=30).aggregate(Avg('age'))

    #Total customer purchase amount
    result=Customer.objects.aggregate(Sum('purchases__amount'))

    #specific customer  total amount purchase
    result=Customer.objects.filter(id=1).aggregate(Sum('purchases__amount'))

    #specific customer count of purchase
    result=Customer.objects.filter(id=3).aggregate(Count('purchases__amount'))

    #how many purchases with the same value
    result=Purchase.objects.values('amount').annotate(Count('amount'))
    print(result)

    #total amount of all purchases by customer
    result=Purchase.objects.values('customer').annotate(Sum('amount'))
    print(result)

    #find the total amount purchased each customer
    result=Customer.objects.annotate(amount_purchased=Sum('purchases__amount')).values('name','amount_purchased')

    # how many times user purchased
    result=Customer.objects.annotate(purchased_times=Count('purchases')).values('name','purchased_times')
    print(result)


    for res in result:
        print(res)

    return HttpResponse(f'Result :{result}')





def blog_post_view(request):
    #this will take return number of comments in each blog .and values() method return this value with dictionary
    result=Blogs.objects.annotate(num_comment=Count('realated_comment')).values('blog_title','num_comment')
    print(result)

    result=Blogs.objects.annotate(num_likes=Sum('related_likes__likes')).values('blog_title','num_likes')
    print(result)
    return HttpResponse(f'result:{result}')





def select_related_View(requesst):

    # posts=Post.objects.all()
    # print(posts)

    # normal_data=[post.author.name for post in posts]

    select_related=Post.objects.all().select_related('author').values('title','desc','author__name')
    print(select_related)


    # return HttpResponse(select_related)



