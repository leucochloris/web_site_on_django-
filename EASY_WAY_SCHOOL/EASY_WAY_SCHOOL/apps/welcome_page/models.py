from django.db import models
from django.utils import timezone


# Create your models here.

class Registration(models.Model):
    user_id = models.IntegerField('ID юзера', primary_key=True, unique=True)  # , auto_created=True, )
    name = models.TextField('Имя юзера')
    surname = models.TextField('Фамилия юзера')
    city = models.TextField('Город юзера')
    age = models.TextField('Возраст юзера')
    level = models.TextField('Уровень владения юзера')
    phone = models.IntegerField('Телефон юзера')
    email = models.TextField('Email юзера', max_length=50, default=None)
    join_date = models.DateTimeField('Дата регистрации')
    is_active = models.BooleanField('Cтатус юзера АКТИВ/НЕ АКТИВНЫЙ', default=0)

    # def __str__(self, **kwargs):
    #     return str(self.user_id), self.name, self.email

    def __str__(self, *args):
        return self.user_id, self.name, self.surname, self.email

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'Клиентов'