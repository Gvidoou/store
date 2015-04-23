from django.forms import ModelForm
from Products.models import Comments


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['title', 'comment']

    def __init__(self, *args, **kwargs):
        super(CommentsForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['comment'].widget.attrs.update({
            'class': 'form-control'
        })