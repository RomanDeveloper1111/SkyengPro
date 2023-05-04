from django.forms import ModelForm
from back.models import UserFile


class FileForm(ModelForm):
    class Meta:
        model = UserFile
        fields = ('file',)
