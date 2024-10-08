from .models import Post, Comment
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

        # label = {
        #     "title": "Title",
        #     "content": "Content",
        # }

        # widgets = {
        #     "title": forms.TextInput(attrs={"placeholder": "No Title"}),
        #     "content": forms.TextInput(attrs={"placeholder": "Empty Content"})
        # }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']