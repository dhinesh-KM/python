from django.shortcuts import render,get_object_or_404,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import  messages
from django.http import JsonResponse,HttpResponse
from invent.models import product
from accounts.models import CustomUser
from .models import Order
from .forms import ProductForm
from django.views.generic.detail import DetailView

# Create your views here.

'''class ProductDetailView(DetailView):
    model = product
    

    def render_to_response(self, context, **response_kwargs):
        # Serialize the object to JSON
        self.object = self.get_object()
        data = { 
            'name': self.object.name,
            'price': str(self.object.price),  # Convert DecimalField to string
            'quantity': str(self.object.quantity),  # Convert DecimalField to string
            'discount': self.object.discount,
        }
        return JsonResponse(data)'''
    


def index(request):
    return render(request,"index.html",{})


def display_all_products(request):
    products = product.objects.all()
    data = [{"id":x.product_id,"name":x.name,"price":str(x.price),"quantity":str(x.name),"discount":str(x.discount)} for x in products]
    return JsonResponse(data, safe=False)

def display(request):
    id = request.GET["pk"]
    try:
        pd = product.objects.get(pk=id)
        print(pd)
        data = {"id":pd.product_id,"name":pd.name,"price":str(pd.price),"quantity":str(pd.name),"discount":str(pd.discount)}
        return JsonResponse(data, safe=False)
    except ObjectDoesNotExist:
        return JsonResponse({"message":"Product id doesnot exists ","status":404},status=404)

def place_order(request):
    if request.method == "POST":
        form = ProductForm(request.POST)   
        if form.is_valid():
            o_product = form.cleaned_data["product_name"]
            o_quantity = form.cleaned_data["quantity"]
            
            user = request.user
            try:
                pr = product.objects.get(name=o_product)
                o_pid = pr.product_id
                print(o_pid)
            except product.DoesNotExist:
                return JsonResponse({'error': 'Product not found',"status":400}, status=400)
            
            u = update(o_pid,o_quantity,request)
            if u == 0:
                p = Order.objects.create(user=user,o_product=o_product,o_quantity=o_quantity,prod=pr)
                t_p = price(o_quantity,pr)
                data = {"product":o_product,"quantity":str(o_quantity),"price":str(t_p)}
                return JsonResponse({'message':"Order placed successfully","bill":data},status = 200)
                
                

            else:
                return redirect('index')
        
    else:
        form = ProductForm()
        return render(request, "order.html", {'form': form})
        

    
def update(id,q,r):
    p = product.objects.get(pk=id)
    if p.quantity <=0:
        messages.warning(r,f"There is no {p.name} in the stock")
        return 1

    elif p.quantity < q:
        messages.warning(r,f"There are only {p.quantity} {p.name} left in the stock")
        return 1
    else:
        p.quantity -= q
        p.save()
        return 0
        
def price(q,pr):
    price = (q * pr.price)-(q(pr.price * (pr.discount/100)))
    return price
    
        
        
    
