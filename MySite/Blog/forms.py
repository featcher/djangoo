from django.forms import ModelForm
from Blog.models import user,first,log,ne

class details(ModelForm):
    class Meta:
        model= user
        fields='__all__'
class one(ModelForm):
    class Meta:
        model= first
        fields='__all__'
class gin(ModelForm):
    class Meta:
        model= log
        fields='__all__'
class new(ModelForm):
    class Meta:
        model= ne
        fields='__all__'