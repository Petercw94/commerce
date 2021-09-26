from django.forms import ModelForm
from auctions.models import Listing

class NewListingForm(ModelForm):
        class Meta:
             model = Listing
             fields = ['title', 'description', 'starting_bid', 'image', 'category',]

        def __init__(self, *args, **kwargs):
            super(NewListingForm, self).__init__(*args, **kwargs)
            self.fields['image'].required = False
            self.fields['category'].required = False