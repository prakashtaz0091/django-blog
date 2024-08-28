from django import forms
from .models import Post,Category, Comment
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget


class CreateBlogForm(forms.ModelForm):
    # content = SummernoteTextField()
    content = forms.CharField(widget=SummernoteWidget(attrs={'height': 300, 'width': 800}))

    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['title', 'content', 'category'] 


    def save(self, commit=True, **kwargs):
        blog = super().save(commit=False)
        
        blog.author = kwargs.get('author')
        if commit:
            blog.save()
        return blog


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


    def save(self, commit=True, **kwargs):
        comment = super().save(commit=False)
        
        comment.author = kwargs.get('commenter')
        comment.post = kwargs.get('post')
        if commit:
            comment.save()
        return comment
