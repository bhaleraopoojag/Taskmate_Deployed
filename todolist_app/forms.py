from todolist_app.models import tasklistmodel
from django import forms

class taskform(forms.ModelForm):
    class Meta:
        model= tasklistmodel
        fields=['task','done']    

    
