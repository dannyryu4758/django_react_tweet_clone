from django import forms
from django.forms import fields

from .models import Tweet


MAX_TWEET_LENGTH = 240


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("해당 글의 길이가 너무 깁니다.")
        return content
