from .models import Product
from django.forms import ModelForm
from  django.forms import TextInput,DateInput

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name','date']

        widgets={
            'name': TextInput(attrs={
                'class':"form-control",
                'placeholder':"Введите название продукта",
            }),
            'date': DateInput(attrs={
                'class': "form-control",
            })
        }