from django import forms
from .models import Album, Image

WORK_CHOICES = (
        ('Commercial', 'Commercial'),
        ('Residential', 'Residential'),
)


class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    type_of_work = forms.ChoiceField(choices=WORK_CHOICES)
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)


class AlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AlbumForm, self).__init__(*args, **kwargs)
        self.fields['cover_photo'].queryset = Image.objects.filter(albums=self.instance)

    class Meta:
        model = Album
        exclude = ['']
