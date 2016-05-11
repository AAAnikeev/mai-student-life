from django import forms

class FeedbackForm(forms.Form):
    text= forms.CharField(label='Text', max_length=100)#widget=forms.Textarea)