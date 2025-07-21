from todolist_app.models import tasklistmodel
from django import forms

class taskform(forms.ModelForm):
    class Meta:
        model= tasklistmodel
        fields=['task','done']    
        
class contactform(forms.Form):
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    message=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

    
