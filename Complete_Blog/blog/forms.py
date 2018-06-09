from django.forms import ModelForm
from .models import Comment, Suggestion, ReplyModel


class BlogFrom(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class SuggestionForm(ModelForm):
    class Meta:
        model = Suggestion
        fields = '__all__'


class ReplyForm(ModelForm):
    class Meta:
        model = ReplyModel
        fields = ['reply']
