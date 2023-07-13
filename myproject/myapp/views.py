from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import OrderForm, HomeForm
from .models import Order, Homecleaning, Feature, Contactform
from django.utils import timezone  




def index(request):
    if request.method == "POST":                    
        name = request.POST.get('name') 
        subject = request.POST.get('subject')            
        email = request.POST.get('email')            
        message = request.POST.get('message')            
        image = request.FILES['attachment']      
            
        print(request.FILES)            
        print(name, subject, email, message, image)            
        Contactform.objects.create(name=name, subject=subject, email=email, message=message, image=image)  
        messages.success(request, f'YOUR MESSAGE IS SENT THANK YOU!!!!.')
        return redirect('index') 

    features = Feature.objects.all()

    return render(request, 'index.html', {'fetures': features})




def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thank you for choosing us.')
            return render(request, 'order_success.html')
    else:
        form = OrderForm

    return render(request, 'order_create.html', {'form': form})


def home_cleaning(request):
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thank you for choosing us.')
            return render(request, 'cleaning_success.html')
    else:
        form = HomeForm
    
    return render(request, 'home_cleaning.html', {'form': form})


def order_success(request):
    
    return render(request, 'order_success.html')


def inner_page(request):
    features = Feature.objects.all()

    
    return render(request, 'inner_page.html', {'fetures': features})


def about(request):
    
    return render(request, 'about.html')


def cleaning_success(request):

    
    return render(request, 'cleaning_success.html')








