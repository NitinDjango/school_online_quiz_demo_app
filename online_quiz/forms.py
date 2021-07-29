from django import forms
from online_quiz.models import school_staff_admin
from online_quiz.models import new_quiz_register
from django.core import validators



def not_more_than_and_no_space(value):
    if len(value) > 50:
        raise forms.ValidationError('Name should be NOT more than 50 characters including space')
    if value.isalnum()==False:
        raise forms.ValidationError("Don't put a space between words use 'hyphen(-)' instead")
def bot(value):
    if len(value)>0:
        raise forms.ValidationError('thanks bot')

class new_quiz_register(forms.ModelForm):
    quiz_name=forms.CharField(label='Name the quiz you want to create',validators=[not_more_than_and_no_space])
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput,validators=[bot])
    class Meta:
        model=new_quiz_register
        fields=['quiz_name']
