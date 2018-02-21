from django import forms

from .models import Photo


class PhotoForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Photo
        fields = ('image', 'content', )


