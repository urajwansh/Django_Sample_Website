from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
            model = Product
            fields = [
                'title',
                'description',
                'price'
            ]

class RawProductForm(forms.Form):
    title       =forms.CharField(label="title",widget=forms.TextInput(attrs={"placeholder":"your title"}))
    description =forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                        attrs={
                            "placeholder":"your description",
                            "class":"new_class_description",
                            "id":"my_id_description",
                            "rows":15,
                            "cols":100
                        }))
    price       =forms.DecimalField(initial=199.99)
