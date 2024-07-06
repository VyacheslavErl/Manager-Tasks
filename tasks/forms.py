from django.forms import ModelForm, TextInput, DateInput, FileInput
from django.forms.utils import ErrorList

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

    def clean(self):
        image = self.cleaned_data.get('image')
        if image.size > 0.1*1024*1024:
            self._errors["image"] = ErrorList(["Файл слишком большой. Размер не должен превышать 2 МБ."])

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
