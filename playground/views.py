from django.forms import DecimalField
from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Customer, Collection, Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q, F
from django.db.models.aggregates import Count, Max, Min, Avg, Sum
from django.db.models import Value, F, Func, ExpressionWrapper
from django.db.models.functions import Concat
from django.contrib.contenttypes.models import ContentType
from tags.models import TaggedItem
from django.db import transaction
from django.db import connection


# @transaction.atomic()
def say_hello(request):

    query_set = Product.objects.all()

    # for product in query_set:
    #     print(product)

    # list(query_set[0:5])

    # query_set.filter().filter().order_by()

    # query_set = Product.objects.count()

    # retrieving objects in detail

    # query_set = Product.objects.all()

    # product = Product.objects.get(pk=0)

    # product = Product.objects.get(pk=1)

    # try:
    #     product = Product.objects.get(pk=0)
    # except ObjectDoesNotExist:
    #     pass

    # product = Product.objects.filter(pk=0).first()

    # exists = Product.objects.filter(pk=0).exists()

    # filtering data

    # query_set = Product.objects.filter(unit_price=20)

    # query_set = Product.objects.filter(unit_price__gt=20)

    # query_set = Product.objects.filter(unit_price__gte=20)

    # query_set = Product.objects.filter(unit_price__lt=20)

    # query_set = Product.objects.filter(unit_price__lte=20)

    # query_set = Product.objects.filter(unit_price__range=(20, 30))

    # query_set = Product.objects.filter(collection__id=1)

    # query_set = Product.objects.filter(collection__id__range=(1, 2, 3))

    # query_set = Product.objects.filter(title__contains='coffee')

    # query_set = Product.objects.filter(title__icontains='coffee')

    # query_set = Product.objects.filter(title__startswith='coffee')

    # query_set = Product.objects.filter(title__endswith='coffee')

    # query_set = Product.objects.filter(last_update__year=2021)

    # query_set = Product.objects.filter(description__isnull=True)

    # excercise

    # customers with .com accounts

    # customers = Customer.objects.filter(email__icontains='.com')

    # collections that dont have a featured products

    # collections = Collection.objects.filter(featured_product__isnull=True)

    # products with low inventory (less than 10)

    # products = Product.objects.filter(inventory__lt=10)

    # order placed by customer with id = 1

    # orders = Order.objects.filter(customer__id=1)

    # order items for products in collection3

    # order_items = OrderItem.objects.filter(product__collection_id=3)

    # complex lookup using q objects

    # Products: inventory < 10 AND price < 20

    # products = Product.objects.filter(inventory__lt=10, unit_price__lt=20)

    # query_set = Product.objects.filter(
    #     inventory__lt=10).filter(unit_price__lt=20)

    # Products: inventory < 10 OR price < 20

    # query_set = Product.objects.filter(
    #     Q(inventory__lt=10) | Q(unit_price__lt=20))

    # query_set = Product.objects.filter(
    #     Q(inventory__lt=10) & Q(unit_price__lt=20))

    # not operator
    # query_set = Product.objects.filter(
    #     Q(inventory__lt=10) & ~Q(unit_price__lt=20))

    # Refferencing fields using f objects

    # query_set = Product.objects.filter(inventory=unit_price) # error
    # query_set = Product.objects.filter(inventory='unit_price') # error

    # query_set = Product.objects.filter(inventory=F('unit_price'))
    # query_set = Product.objects.filter(inventory=F('collection__id'))

    # sorting data

    # query_set = Product.objects.order_by('title')
    # query_set = Product.objects.order_by('-title')
    # query_set = Product.objects.order_by('unit_price','-title')
    # query_set = Product.objects.order_by('unit_price', '-title').reverse()
    # query_set = Product.objects.filter(collection__id=1).order_by('unit_price')
    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('unit_price')
    # product = Product.objects.latest('unit_price')

    # limiting results

    # query_set = Product.objects.all()[:5]
    # query_set = Product.objects.all()[5:10]

    # searching fields to query
    # query_set = Product.objects.values('id', 'title', 'colection__title')
    # query_set = Product.objects.values_list('id', 'title', 'colection__title')

    # select products that have been ordered
    # and sort them by title

    # query_set = Product..objects.filter(
    #     id__in=(OrderItemobjects.values('product_id').distinct())).order_by('title')

    # query_set = Product.objects.only('id', 'title')

    # query_set = Product.objects.defer('description')

    # query_set = Product.objects.select_related('collection').all()
    # query_set = Product.objects.select_related('collection__someOtherField').all()

    # select related (1)
    # prefetch related (n)

    # query_set = Product.objects.prefetch_related('promotions').all()

    # query_set = Product.objects.prefetch_related(
    #     'promotions').select_related('collection').all()

    # get the last 5 orders with their customer
    # and items (incl product)

    # query_set = Order.objects.select_related(
    #     'customer').prefetch_related('orderitem_set__product').order_by('-placed_at')[0:5]

    # agreegate methods
    # result = Product.objects.aggregate(Count('id'))

    # result = Product.objects.aggregate(
    #     count=Count('id'),
    #     min_price=Min('unit_price')
    # )

    # result = Product.objects.filter(collection__id=1).aggregate(
    #     count=Count('id'),
    #     min_price=Min('unit_price')
    # )

    # query_set = Customer.objects.annotate(is_new=True) #error

    # query_set = Customer.objects.annotate(is_new=Value(True))

    # query_set = Customer.objects.annotate(new_id=F('id'))

    # query_set = Customer.objects.annotate(new_id=F('id') + 1)

    # query_set = Customer.objects.annotate(
    #     # Concat
    #     full_name=Func(
    #         F('first_name'),
    #         Value(' '),
    #         F('last_name'),
    #         function='CONCAT')
    # )

    # same way to do that

    # query_set = Customer.objects.annotate(
    #     # concat
    #     full_namre=Concat('first_name', Value(' '), 'last_name')
    # )

    # grouping data

    # query_set = Customer.objects.annotate(
    #     orders_count=Count('order')
    # )

    # working with expression wrappers

    # discounted_price = ExpressionWrapper(
    #     F('unit_price')*0.8, output_field=DecimalField())

    # qury_set = Product.objects.annotate(
    #     discountedprice=discounted_price
    # )

    # querying generic relationships
    # content_type = ContentType.objects.get_for_model(Product)

    # query_set = TaggedItem.objects \
    #     .select_related('tag') \
    #     .filter(
    #         content_type=content_type,
    #         object_id=1
    #     )

    # custom managers
    # query_set = TaggedItem.objects.get_tags_for(Product,1)

    # understanding queryset cache
    # query_set = Product.objects.all()
    # list(query_set)
    # query_set[0]

    # inserting objects

    # collection = Collection()
    # collection.title = 'Video Games'
    # # collection.featured_product = Product(pk=1)
    # collection.featured_product_id = 1

    # collection = Collection(title='Video Games')

    # collection = Collection()
    # collection.name = 'Video Games'
    # collection.featured_product = Product(pk=1)
    # collection.save()
    # collection.id

    # collection = Collection.objects.create(
    #     name='a',
    #     featured_product_id=1
    # )
    # collection.save()

    # updating objects
    # collection = Collection(pk=11)
    # collection.title = 'Games'
    # collection.featured_product = None
    # collection.save()

    # just updating the featured product
    # something crazy happening here
    # collection = Collection(pk=11)
    # collection.title = ''  # internally this things happens
    # collection.featured_product = None
    # collection.save()

    # first get it from the database and then update
    # collection = Collection.objects.get(pk=11)
    # collection.featured_product = None
    # collection.save()

    # reading first object get performance penalty (not)
    # dont try to prematurily optimize your code

    # how to avoid

    # collection = Collection.objects.filter(pk=11).update(
    #     featured_product=None
    # )

    # deleting objects

    # collection = Collection(pk=1)
    # collection.delete()

    # to delete multiple objects
    # Collection.objects.filter(id__gt=5).delete()

    # transactions
    # atomic way - means all changes should be save together
    # if any change failed - the all changes should be rollback

    # some other code here which is not part of a transaction

    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = 1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()

    # for exception
    # with transaction.atomic():
    #     order = Order()
    #     order.customer_id = 1
    #     order.save()

    #     item = OrderItem()
    #     item.order = order
    #     item.product_id = -1
    #     item.quantity = 1
    #     item.unit_price = 10
    #     item.save()

    # executing raw sql queries

    # query_set = Product.objects.raw('SELECT * FROM store_product')

    # this queryset is different from previous all queryset

    # query_set = Product.objects.raw('SELECT * from store_product')
    # query_set.fiter
    # query_set.annotate
    # does not present

    # query_set = Product.objects.raw('SELECT id, title FROM store_product')

    # cursor = connection.cursor()
    # cursor.execute('Any sql query')
    # cursor.close()

    # we can use cursor with statement

    # with connection.cursor() as cursor:
    #     cursor.callproc('get_customers,[1,2,'a'])
    #     cursor.execute()

    return render(
        request,
        'hello.html',
        {'name': 'kunal', 'products': list(query_set)}
    )
