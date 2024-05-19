from django.forms import ModelForm, TextInput, DateInput, FileInput

from tasks.models import TaskModel, CommentModel


class TaskForm(ModelForm):
    class Meta:
        model = TaskModel
        fields = ['name', 'text', 'do_before', 'image']

        widgets = {
            'name': TextInput(attrs={
                'type': 'text',
                'placeholder': 'Название'
            }),
            'text': TextInput(attrs={
                'type': 'text',
                'placeholder': 'Описание'
            }),
            'do_before': DateInput(attrs={
                'type': 'date'
            }),
            'image': FileInput(attrs={
                'type': 'file',
                'accept': "image/*"
            }),

        }


class CommentForm(ModelForm):
    class Meta:
        model = CommentModel
        fields = ['text']

        widgets = {
            'text': TextInput(attrs={
                'type': 'text',
                'class': 'add-comment-field',
                'placeholder': 'Добавить комментарий...'}
            )
        }
