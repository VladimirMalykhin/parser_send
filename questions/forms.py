from django import forms

from questions.models import SaveUrl
from questions.choices import *


class PostForm(forms.ModelForm):

    class Meta:
        model = SaveUrl
        exclude = [" "]
