from django.forms import ModelForm, Textarea, NumberInput, DateInput
from .models import Item


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["date", "name", "amount", "distance"]
        widgets = {
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату',
            }),
            "name": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите наименование',
            }),
            "amount": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество',
            }),
            "distance": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите расстояние',
            })
        }
