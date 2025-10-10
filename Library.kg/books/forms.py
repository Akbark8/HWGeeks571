from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']
        labels = {
            'rating': 'Ваша оценка',
            'text': 'Ваш отзыв'
        }
