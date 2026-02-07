from django import forms
from .models import Resource
from .models import Rating

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'category', 'college', 'department', 'semester', 'file']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Enter short description...'}),
        }


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stars', 'comment']
        widgets = {
            'stars': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Leave a comment...'}),
        }