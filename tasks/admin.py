from django.contrib import admin
from tasks.models import TaskModel, CommentModel

admin.site.register(TaskModel)
admin.site.register(CommentModel)

# Register your models here.
