from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    __forbidden_words = ['казино',
                         'криптовалюта',
                         'крипта',
                         'биржа',
                         'дешево',
                         'бесплатно',
                         'обман',
                         'полиция',
                         'радар']

    class Meta:
        model = Product
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        for word in self.__forbidden_words:
            if word in name.lower() or word in description.lower():
                raise forms.ValidationError(f'В названии или в описании использовано запрещенное слово')
        return cleaned_data
