from django import forms


class ByersDetailForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=40, error_messages={'max_length': 'Слишком много символов',
                                                                       'required': 'Это поле обязательно для заполнения', },
                           widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'placeholder': 'E-mail'}))
    phone = forms.IntegerField(label='Телефон', widget=forms.NumberInput(attrs={'placeholder': 'Телефон'}))
    country = forms.CharField(label='Страна', max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Страна'}))
    city = forms.CharField(label='Город', max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Город'}))
    street = forms.CharField(label='Улица', max_length=60, widget=forms.TextInput(attrs={'placeholder': 'Улица'}))
    house = forms.IntegerField(label='Дом', widget=forms.NumberInput(attrs={'placeholder': 'Дом'}))
    flat = forms.IntegerField(label='Квартира', widget=forms.NumberInput(attrs={'placeholder': 'Квартира'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Введите сообщение'}))
