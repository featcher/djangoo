from django.forms import ModelForm
from App4.models import upload


class user(ModelForm):
    class Meta:
        model = upload
        fields = "__all__"
