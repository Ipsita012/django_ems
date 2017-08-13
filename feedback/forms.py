from django import forms
from .models import Feedback

class FeedbackAddForm(forms.ModelForm):
  comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 60, 'style': 'resize:none;'}))

  class Meta:
    model = Feedback
    fields = ('name', 'category', 'email', 'subject', 'is_read')


class FeedbackForm(forms.ModelForm):
  comment = forms.CharField(widget=forms.Textarea(attrs={'rows': 6, 'cols': 60, 'style': 'resize:none;'}))
  created_on = forms.CharField(widget=forms.Textarea(attrs={'readonly': 'readonly', 'rows': 1, 'style': 'resize:none;'}))

  class Meta:
    model = Feedback
    fields = '__all__'
