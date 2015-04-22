from django.forms import ModelForm
from Products.models import Comments


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['title', 'comment']