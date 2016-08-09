from django import forms
from .models import Album, Image

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    type_of_work = forms.ChoiceField(choices = (('Commercial', 'Commercial'), ('Residential', 'Residential')))
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


class AlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.fields['cover_photo'].queryset = Image.objects.filter(albums=self.instance)

    class Meta:
        model = Album
        exclude = ['']
