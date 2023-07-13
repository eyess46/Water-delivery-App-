from django import forms
from django.forms import RadioSelect
from .models import Order, Homecleaning



PRICE_OPTIONS = (
    ('9000', 'Full Tanker - ($9000)'),
    ('4000', 'Half Tanker - ($4000)'),
)

class OrderForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=100)
    email = forms.EmailField()
    address = forms.TextInput()
    date_needed = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    price_options = forms.ChoiceField(choices= PRICE_OPTIONS, widget=RadioSelect)
    payment_slip = forms.ImageField()

    class Meta:
        model = Order
        fields =['first_name', 'last_name', 'phone_number', 'email', 'address', 'date_needed', 'price_options', 'payment_slip']

    def clean(self):
        print('clean method called')
        cleaned_data = super().clean()
        full = cleaned_data.get('price_options') == str(PRICE_OPTIONS[0][0])
        half = cleaned_data.get('price_options') == str(PRICE_OPTIONS[0][0])
        quantity = 0
        if full:
            quantity = 1
        elif half:
            quantity = 0.5

        cleaned_data['quantity'] = quantity
        return cleaned_data

    

class HomeForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=100)
    email = forms.EmailField()
    address = forms.TextInput()
    date_needed = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    about_services = forms.TextInput()


    class Meta:
        model = Homecleaning
        fields =['first_name', 'last_name', 'phone_number', 'email', 'address', 'date_needed', 'about_services']