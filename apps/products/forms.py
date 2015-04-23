from django.forms import ModelForm
from django.forms.widgets import Input, Textarea

from apps.products.models import Comments


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['title', 'comment']
        widgets = {
            'comment': Textarea(attrs={'class': 'form-control'}),
            'title': Input(attrs={'class': 'form-control'}),
        }
