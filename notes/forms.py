from django import forms
from .models import Notes


class NotesFrom(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb-5'})
        }
        labels = {'title': 'Title', 'text': 'Write your text here'}

    def clean_title(self):
        title = self.cleaned_data['title']  # returned by the form
        if 'Django' not in title:
            raise forms.ValidationError('We only accept notes about Django!')
        return title
