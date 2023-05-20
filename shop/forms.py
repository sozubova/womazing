from django import forms
from . import models


# class ProductForm(forms.Form):
class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=models.Category.objects.all(), empty_label=None,
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    new_category = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    discount_price = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'Цена со скидкой'}))

    class Meta:
        model = models.Product
        fields = ['title', 'category', 'new_category', 'cover', 'price', 'discount_price', 'size', 'color']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Название', 'label': 'Название'}),
            'category': forms.RadioSelect(attrs={'placeholder': 'Категория', 'label': 'Категория'}, ),
            'new_category': forms.TextInput(attrs={'placeholder': 'Новая категория', 'label': 'Новая категория'}, ),
            'price': forms.NumberInput(attrs={'placeholder': 'Цена'}),
            # 'discount_price': forms.NumberInput(attrs={'placeholder': 'Цена со скидкой'}),
            'size': forms.CheckboxSelectMultiple(attrs={'class': 'size-choices'}),
            # 'size': forms.RadioSelect(attrs={'class': 'size-choices'}),
            'color': forms.CheckboxSelectMultiple(attrs={'class': 'color-choices'}),
        }
