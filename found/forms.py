from django import forms
from found.models import PageF, KindF

from django.contrib.auth.models import User

class KindFForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the found name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = KindF
        fields = ('name',)


class PageFForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, widget=forms.TextInput, help_text="Please enter the nothing of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = PageF
        exclude = ('category',)
        fields = ('title', 'url', )