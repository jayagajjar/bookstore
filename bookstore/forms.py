from django import forms
from .models import *


class BookImageForm(forms.ModelForm):
    class Meta:
        model = BooksImages
        fields = ['name', 'book_img']