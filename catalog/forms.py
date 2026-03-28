from django import forms
from .models import Product

FORBIDDEN_WORDS = [
    'казино', 'криптовалюта', 'крипта', 'биржа',
    'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    #  Стилизация формы
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

        # чекбокс отдельно
        if 'is_published' in self.fields:
            self.fields['is_published'].widget.attrs.update({'class': 'form-check-input'})

    #  Валидация name
    def clean_name(self):
        name = self.cleaned_data.get('name').lower()

        for word in FORBIDDEN_WORDS:
            if word in name:
                raise forms.ValidationError(f'Запрещено использовать слово: {word}')

        return name

    #  Валидация description
    def clean_description(self):
        description = self.cleaned_data.get('description').lower()

        for word in FORBIDDEN_WORDS:
            if word in description:
                raise forms.ValidationError(f'Запрещено использовать слово: {word}')

        return description

    #  Валидация price
    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 0:
            raise forms.ValidationError('Цена не может быть отрицательной')

        return price