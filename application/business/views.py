from django.shortcuts import render, redirect
from .models import Company, Product, Order , ItemList , Status 
from datetime import datetime
from django.http import JsonResponse

def home_page(request):
    return render(request,'home.html')

# def order_entry(request):
#     companies = Company.objects.all()
#     products = Product.objects.all()
    
#     if request.method == 'POST':
#         company_id = request.POST['company']
#         product_id = request.POST['product']
#         quantity = request.POST['quantity']
#         address=request.POST['address']
#         #amount = request.POST['amount']
        
#         company = Company.objects.get(pk=company_id)
#         product = Product.objects.get(pk=product_id)
#         amount = int(quantity)*int(product.price) 
        
#         order = Orders(companyName=company, product=product, quantity=quantity, amount=amount,address=address)
#         order.save()

#         return success_page(request,amount)

#     return render(request, 'orders.html', {'companies': companies, 'products': products})

def order_entry(request):
    companies = Company.objects.all()
    products = Product.objects.all()
    
    if request.method == 'POST':
        company_id = request.POST['company']
        product_id = request.POST['product']
        quantity = request.POST['quantity']
        state = request.POST['state']
        city = request.POST['city']
        landmark = request.POST['landmark']
        area = request.POST['area']
        pincode = request.POST['pincode']
        house_name = request.POST['houseName']

        # Retrieve company and product instances
        company = Company.objects.get(pk=company_id)
        product = Product.objects.get(pk=product_id)

        # Calculate the amount based on quantity and product price
        amount = int(quantity) * int(product.price)

        # things from Customer order track 
        customer_id=request.user.id
        statuss= Status.objects.get(pk=1)
        date_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  
        # Create a new order instance and save it to the database
        order = Order(
            companyName=company,
            product=product,
            quantity=quantity,
            amount=amount,
            state=state,
            city=city,
            landmark=landmark,
            area=area,
            pincode=pincode,
            houseName=house_name,
            # C O T things 
            customerId=customer_id,
            status=statuss,
            dateTime=date_time
        )
        order.save()
        
        
       

        # Redirect to a success page with the order amount
        return success_page(request,amount)

    return render(request, 'orders.html', {'companies': companies, 'products': products})

def track_page(request):
     
     target_statuses = Status.objects.filter(type__in=["Order-Placed", "Order-Accepted"])
     customer_orders = Order.objects.filter(
     customerId=request.user.id,
     status__in=target_statuses
      )
    # customer_orders = Orders.objects.all()
     return render(request,'track.html',{'CustomerOrders':customer_orders})

def ordered_page(request):
     target_statuses = Status.objects.filter(type__in=["Settled"])
     customer_orders = Order.objects.filter(
     customerId=request.user.id,
     status__in=target_statuses
      )
     return render(request,'ordered.html',{'CustomerOrders':customer_orders})

def detailed_page(request,pk):
    order=Order.objects.get(pk=pk)
    return render(request,'detailed.html',{'order':order})

def user_page(request):
    return render(request,'user.html')

def success_page(request,amount):
    return render(request, 'success.html',{'amount':amount})

def price_list(request):
    priceList= ItemList.objects.all()
    material=ItemList.objects.get(pk=6)
    return render(request,'price_list.html',{'items':priceList , 'material':material})

def price_list_update(request,pk):
    material = ItemList.objects.get(pk=pk)
    priceList= ItemList.objects.all()
    return render(request,'price_list.html',{'material':material, 'items':priceList})

def health(request):
    return JsonResponse({"status": "ok"})


