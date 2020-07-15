from django import forms
from blog_app.models import Author, Category, Post


class AuthorCreateForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Author
        # Must use fields or exclude
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
                    'name': 'Author Name',
                }


class CategoryCreateForm(forms.ModelForm):
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Category
        # Must use fields or exclude
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
                    'name': 'Category Name',
                }


class PostCreateForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # slug = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # category = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        # Must use fields or exclude
        fields = ['title', 'slug', 'description', 'post_image', 'category', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            # 'post_image': forms.FileField(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
        }

        labels = {
                    'title': 'Post Title',
                    'slug': 'Post Slug',
                    'description': 'Post Description',
                }
