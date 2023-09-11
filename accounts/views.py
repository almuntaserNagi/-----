from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Customer
from mirror.models import *
from mirror.forms import *  # Replace 'CustomerForm' with your actual form class
from .forms import *

from django.contrib.auth import authenticate, login

from .forms import OrderForm

from django.shortcuts import get_object_or_404

from django.shortcuts import render
from .models import *


from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect

from django.contrib import messages  # Import the messages module

def login_custom(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_superuser:
                # Redirect to admin panel
                login(request, user)
                return redirect('admin:index')
            
            
            elif Group.objects.filter(name__in=['أمين الصندوق', 'رئيس قسم المتابعة', 'لجنة النزول']).filter(user=user).exists():
                # Redirect to admin panel for specific groups
                login(request, user)
                return redirect('admin:index')
                
            elif user.groups.filter(name='العملاء').exists():
                # Redirect to the 'politics_agree' page for customers
                login(request, user)
                customer = Customer.objects.get(user=request.user)
                exhibition=Exhibition.objects.filter(customer=customer)
                ex=exhibition.last()
                if customer.stop_at =='license':
                    return redirect('admin:index')
                    
                if customer.stop_at is not 'add_exhibition_details':
                    return redirect(customer.stop_at)
                    
                if customer.stop_at:
                    return redirect('add_exhibition_details',exhibition_id=ex.pk)
                

            else:
                # Handle other cases or provide an error message
                messages.error(request, 'Invalid user group')
        else:
            # Handle invalid login credentials or provide an error message
            messages.error(request, 'Invalid login credentials')

    return render(request, 'login.html', {})

def customer_document1(request):
            customer = Customer.objects.get(user=request.user)
            customer.stop_at='customer_doc1'
            customer.save()
            logout(request)
                
                # Authenticate the user again with their identifyNo and password
            identifyNo = customer.identifyNo  # Get the user's identifyNo
            password = request.POST.get('password')  # Get the password from the form
                
                # Authenticate the user
            user = authenticate(request, username=identifyNo, password=identifyNo)
                
            if user is not None:
                    # Login the user again
                login(request, user)
            
    # Retrieve the necessary objects
        
            customer = Customer.objects.get(user=request.user)
            exhibitions = Exhibition.objects.filter(customer=customer)
            
        
            for exhibition in exhibitions:
                    implication = Implication.objects.get(pk=exhibition.implication.pk)
                    exhibition=Exhibition.objects.get(customer=customer)
            # customer.stop_at='upload_assets'
            # customer.save()
            # logout(request)
            
            # # Authenticate the user again with their identifyNo and password
            # identifyNo = customer.identifyNo  # Get the user's identifyNo
            # password = request.POST.get('password')  # Get the password from the form
            
            # # Authenticate the user
            # user = authenticate(request, username=identifyNo, password=identifyNo)
            
            # if user is not None:
            #     # Login the user again
            #         login(request, user)
            #         # return redirect('upload_assets')
        # Pass the objects to the template context
            context = {
                'customer': customer,
                'exhibition': exhibition,
                'implication': implication,
            }

            return render(request, 'csutomerDocs1.html', context)

def customer_detail(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    exhibition = get_object_or_404(Exhibition, customer=customer)
    exhibitions = Exhibition.objects.filter(customer=customer)
    orders = Orders.objects.filter(exhibition__customer=customer)
    
    if request.method == 'POST':
        form = CustomerDetailsForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            
            # Authenticate and login the user
            username = form.cleaned_data['identifyNo']
            password = form.cleaned_data['identifyNo']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('insure_of_data')
            
            
    else:
        form = CustomerDetailsForm(instance=customer)
    
    exhibition_forms = []
    for exhibition in exhibitions:
        if request.method == 'POST':
            exhibition_form = ExhibitionDetailsForm(request.POST, instance=exhibition)
        else:
            exhibition_form = ExhibitionDetailsForm(instance=exhibition)
        exhibition_forms.append(exhibition_form)
    
    if request.method == 'POST':
        all_forms_valid = all(form.is_valid() for form in exhibition_forms)
        if all_forms_valid:
            for exhibition_form in exhibition_forms:

                exhibition_form.save()
                Exhibitiondetail =ExhibitionDetails.objects.get(pk=exhibition.pk)
                Exhibitiondetail.record_number=exhibition_form.cleaned_data['record_number']
                Exhibitiondetail.save()
                return redirect('insure_of_data')
    order_form = OrderForm()
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.exhibition = exhibition  # Set the exhibition of the order to the one associated with the customer
            order.active = False
            order.order_status='order_proccing'
            order.save()
              

        customer.stop_at='confirm_order'
        customer.save()
        logout(request)
        
        # Authenticate the user again with their identifyNo and password
        identifyNo = customer.identifyNo  # Get the user's identifyNo
        password = request.POST.get('password')  # Get the password from the form
        
        # Authenticate the user
        user = authenticate(request, username=identifyNo, password=identifyNo)
        
        if user is not None:
            # Login the user again
            login(request, user)

            return redirect('confirm_order')
    
    context = {
        'form': form,
        'customer': customer,
        'exhibition_forms': exhibition_forms,
        'order_form': order_form,
        'orders': orders,
    }
    return render(request, 'insureOfData.html', context)
# def customer_detail(request):
#     user = request.user
#     customer = Customer.objects.get(user=user)
#     exhibitions = Exhibition.objects.filter(customer=customer)
#     orders = Orders.objects.filter(exhibition__customer=customer)
    
#     if request.method == 'POST':
#         form = CustomerDetailsForm(request.POST, instance=customer)
#         if form.is_valid():
#             form.save()
            
#             # Authenticate and login the user
#             username = form.cleaned_data['identifyNo']
#             password = form.cleaned_data['identifyNo']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
            
            
#     else:
#         form = CustomerDetailsForm(instance=customer)
    
#     exhibition_forms = []
#     for exhibition in exhibitions:
#         if request.method == 'POST':
#             exhibition_form = ExhibitionDetailsForm(request.POST, instance=exhibition)
#         else:
#             exhibition_form = ExhibitionDetailsForm(instance=exhibition)
#         exhibition_forms.append(exhibition_form)
    
#     if request.method == 'POST':
#         all_forms_valid = all(form.is_valid() for form in exhibition_forms)
#         if all_forms_valid:
#             for exhibition_form in exhibition_forms:
#                 exhibition_form.save()
                
#     order_form = OrderForm()
#     if request.method == 'POST':
#         for exhibition in exhibitions:
#             order_form = OrderForm(request.POST)
#             if order_form.is_valid():
#                 order = order_form.save(commit=False)
#                 order = Orders(exhibition=exhibition, active=False)  # Assuming you want to associate the order with the first exhibition
#                 order.save()
#                 return redirect('fourthpage')
    
#     context = {
#         'form': form,
#         'customer': customer,
#         'exhibition_forms': exhibition_forms,
#         'order_form': order_form,
#         'orders': orders,
#     }
#    return render(request, 'insureOfData.html', context)
# def customer_detail(request):
#     user = request.user  # Assuming the user is authenticated
#     customer = Customer.objects.get(user=user)  # Retrieve the customer object
#     exhibitions = Exhibition.objects.filter(customer=customer)
    
#     if request.method == 'POST':
#         form = CustomerDetailsForm(request.POST, instance=customer)
#         if form.is_valid():
#             form.save()  # Save the updated customer data
#              # Redirect to success page or the same view
#     else:
#         form = CustomerDetailsForm(instance=customer)
    
#     exhibition_forms = []
#     for exhibition in exhibitions:
#         if request.method == 'POST':
#             exhibition_form = ExhibitionDetailsForm(request.POST, instance=exhibition)
#         else:
#             exhibition_form = ExhibitionDetailsForm(instance=exhibition)
#         exhibition_forms.append(exhibition_form)
    
#     if request.method == 'POST':
#         all_forms_valid = all(form.is_valid() for form in exhibition_forms)
#         if all_forms_valid:
#             for exhibition_form in exhibition_forms:
#                 exhibition_form.save()  # Save each updated exhibition data
    
#     context = {
#         'form': form,
#         'customer': customer,
#         'exhibition_forms': exhibition_forms,
#     }
#     return render(request, 'insureOfData.html', context)

# def customer_detail(request):
#     user = request.user  # Assuming the user is authenticated
#     customer = Customer.objects.get(user=user)  # Retrieve the customer object
#     exhibitions = Exhibition.objects.filter(customer=customer)
    
#     if request.method == 'POST':
#         form = CustomerForm(request.POST, instance=customer)
#         if form.is_valid():
#             form.save()  # Save the updated customer data
#             return redirect('fourthpage')  # Redirect to success page or the same view
#     else:
#         form = CustomerForm(instance=customer)
    
#     exhibition_forms = []
#     for exhibition in exhibitions:
#         exhibition_form = ExhibitionForm(instance=exhibition)
#         exhibition_forms.append(exhibition_form)
    
#     context = {
#         'form': form,
#         'customer': customer,
#         'exhibition_forms': exhibition_forms,
#     }
#     return render(request, 'insureOfData.html', context)

# def customer_detail(request):
#     user = request.user  # Assuming the user is authenticated
#     customer = Customer.objects.get(user=user)  # Retrieve the customer object
#     exhibitions = Exhibition.objects.filter(customer=customer)
#     if request.method == 'POST':
#         form = CustomerForm(request.POST, instance=customer)
#         if form.is_valid():
#             form.save()  # Save the updated data
#             return redirect('fourthpage')  # Redirect to success page or the same view
#     else:
#         form = CustomerForm(instance=customer)

#     context = {
#         'form': form,
#         'customer': customer,
#         'exhibitions': exhibitions,
#     }
#     return render(request, 'insureOfData.html', context)