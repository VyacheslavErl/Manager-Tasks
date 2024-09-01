from django.db import models
from users.models import UserModel
from companies.models import CompanyModel
# Create your models here.


PRIORITIES = (
    (0, 'Нет приоритета'),
    (1, 'Низкий'),
    (2, 'Средний'),
    (3, 'Высокий')
)


class TaskModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField("Название", max_length=22)
    text = models.TextField("Описание")
    do_before = models.DateField("Дата окончания задачи")
    creation_date = models.DateField("Дата создания задачи", auto_now=True)
    image = models.ImageField("Изображение", upload_to="tasks_image/", default='no_image.png', blank=True)
    priority = models.IntegerField("Приоритет", choices=PRIORITIES, default=0)
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True)
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE, null=True)


class CommentModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField('Текст', max_length=250)
    creation_date = models.DateField('Дата создания', auto_now=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    task = models.ForeignKey(TaskModel, on_delete=models.CASCADE)