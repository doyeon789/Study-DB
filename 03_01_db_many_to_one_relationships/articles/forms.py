from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

class CommentForm(forms.MdoelForm):
    class Meta:
        model = Comment
        fields = '__all__'