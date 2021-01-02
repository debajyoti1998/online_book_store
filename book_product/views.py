from django.shortcuts import render,HttpResponse
from book_product.models import add_product

# Create your views here.

def product_added(request):
    if request.method=='POST':
        product_name=request.POST['product_name']
        product_price=request.POST['product_price']
        tittle=request.POST['tittle']
        image = request.FILES['image']

        product=add_product(product_name=product_name,product_price=product_price,tittle=tittle,image=image)
        product.save()
        return HttpResponse('product save')
    else:
        return render(request,'book_product/input_product.html')


def product_index(request):


    # all_products = Products.objects.all()
    products = add_product.objects.filter
    # data = serializers.serialize('json', all_products )
    # print(data)


    context = {
        "products":products,
    }
    return render(request,'book_product/view_product.html' , context)

    