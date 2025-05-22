from django import forms
from .models import Listing


class WineForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name of wine',
            'wine_colour': 'Wine colour',
            'country': 'Country of origin',
            'taste_profile': 'Taste profile',
            'Price': '€',
        }

        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'border-black listing-form-input'
