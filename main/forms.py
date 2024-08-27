from django import forms
from .models import Post,Category
class CreateBlogForm(forms.ModelForm):
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
