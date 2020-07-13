from django import forms
from .models import Author, Category, Post


class AuthorCreateForm(forms.ModelForm):
    # roll = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # std_class = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # gender = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Author
        # Must use fields or exclude
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
