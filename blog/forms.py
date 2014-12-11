from django.forms import ModelForm

class CommentForm(ModelForm):
    class Meta:
        model = comment
        fields = ['user', 'content']
