from django.forms import ModelForm
from .models import Listing


class ListingForm(ModelForm):
    class Meta:
        model = Listing
        fields = [
            'title',
            'price',
            'num_bed',
            'num_bath',
            'sq_ft',
            'address',
            'images'
        ]
