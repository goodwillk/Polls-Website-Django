from django import forms
from .models import SuggestQuestion

# class SuggestQuestion(forms.Form):
#     firstName = forms.CharField(max_length=100)
#     lastName = forms.CharField(max_length=100)
#     question = forms.CharField(max_length=300)

class SuggestQuestionForm(forms.ModelForm):
    class Meta:
        model = SuggestQuestion
        fields = "__all__"
