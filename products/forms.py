from django import forms

from products.models import ProductCommentModel


class CommentFormModel(forms.ModelForm):
    class Meta:
        model = ProductCommentModel
        exclude = ['products']
