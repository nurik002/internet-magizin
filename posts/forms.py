from django import forms

from posts.models import PostModel


class PostCommentFormModel(forms.ModelForm):
    class Meta:
        model = PostModel
        exclude = ['post', 'created_at']
