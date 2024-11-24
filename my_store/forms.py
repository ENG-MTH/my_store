from unicodedata import category

from django import forms
from my_store.models import *
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description','category','image']


        def clean_price(self):
            price = self.cleaned_data.get('price')
            if price <= 0:
                raise forms.ValidationError('Price must be a positive number')
            return price

        def clean_image(self):
            image= self.cleaned_data('image')
            if image:
                if image.size > 2 * 1024 * 1024:
                    raise forms.ValidationError("Image is too big (>2MB)")
                if not image.content_type in ['image/jpeg', 'image/png']:
                    raise forms.ValidationError("Image does not have a content type")
            return image

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
