from django.forms import ModelForm
from myasso.models import Adherent

class AdherentForm(ModelForm):
    class Meta:
        model = Adherent
        fields = '__all__'

    