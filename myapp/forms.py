from django import forms
from myapp.models import FaceEmotion

class FaceEmotionForm(forms.ModelForm):

    class Meta:
        model = FaceEmotion
        fields= ['image']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].widget.attrs.update({'class':'form-control'})