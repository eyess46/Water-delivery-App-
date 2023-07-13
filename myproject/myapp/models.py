from django.db import models





class Order(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    date_needed = models.DateField()
    price_options = models.IntegerField(choices=((9000, 'Full Tanker'), (4000, 'Half Tanker')))
    payment_slip = models.ImageField(upload_to='payment_slip/')
    created_at = models.DateTimeField(auto_now_add=True)


class Homecleaning(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    date_needed = models.DateField()
    about_services = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



class Feature(models.Model):
    
    name = models.CharField(max_length=100) 
    details = models.CharField(max_length=500)


class Contactform(models.Model):
    name = models.CharField(max_length= 100)
    email = models.EmailField(unique= True)
    subject = models.CharField(max_length= 100)
    message = models.CharField(max_length= 900)
    image = models.ImageField(upload_to= "images/")
