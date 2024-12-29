from django import forms
from .models import Achievement
from .models import Review


class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['title', 'description']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'Напишите ваш отзыв здесь...', 'rows': 4}),
        }
